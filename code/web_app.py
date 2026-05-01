#!/usr/bin/env python3

from __future__ import annotations

import csv
import io
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List

import streamlit as st

from triage import CorpusIndex, load_corpus
from triage.engine import triage_ticket
from triage.models import TicketInput


st.set_page_config(
    page_title="Support Triage Agent",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource(show_spinner=False)
def get_index(data_dir: str) -> CorpusIndex:
    docs = load_corpus(data_dir)
    return CorpusIndex(docs)


def _find_data_directories() -> list[str]:
    root = Path(".").resolve()
    options: list[str] = []
    data_root = root / "data"
    if data_root.exists() and data_root.is_dir():
        options.append("data")
        for child in sorted(data_root.iterdir()):
            if child.is_dir():
                options.append(str(Path("data") / child.name))
    else:
        for child in sorted(root.iterdir()):
            if child.is_dir():
                options.append(child.name)
    return options


def _normalize_company(company: str) -> str:
    c = (company or "").strip().lower()
    if c in {"hackerrank", "claude", "visa"}:
        return c
    return "none"


def _status_badge(status: str) -> str:
    if status == "escalated":
        return ":red[Escalated]"
    return ":green[Replied]"


def _render_decision(decision: Dict[str, str]) -> None:
    col1, col2, col3 = st.columns([1, 1, 1])
    col1.metric("Status", decision["status"])
    col2.metric("Request Type", decision["request_type"])
    col3.metric("Product Area", decision["product_area"])

    st.markdown(f"### {_status_badge(decision['status'])}")
    st.markdown("#### Response")
    st.write(decision["response"])
    st.markdown("#### Justification")
    st.caption(decision["justification"])


def _rows_to_csv(rows: List[Dict[str, str]]) -> bytes:
    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=[
            "issue",
            "subject",
            "company",
            "response",
            "product_area",
            "status",
            "request_type",
            "justification",
        ],
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return out.getvalue().encode("utf-8")


def _parse_uploaded_csv(file_bytes: bytes) -> List[TicketInput]:
    text = file_bytes.decode("utf-8")
    reader = csv.DictReader(io.StringIO(text))
    rows: List[TicketInput] = []
    for row in reader:
        lower = {k.lower(): v for k, v in row.items()}
        rows.append(
            TicketInput(
                issue=(lower.get("issue") or "").strip(),
                subject=(lower.get("subject") or "").strip(),
                company=_normalize_company(lower.get("company") or ""),
            )
        )
    return rows


def render_single_ticket(index: CorpusIndex) -> None:
    st.subheader("Single Ticket Triage")
    st.caption("Triage one support request and inspect routing decisions instantly.")

    with st.form("single_ticket_form", clear_on_submit=False):
        company = st.selectbox(
            "Company",
            options=["None", "HackerRank", "Claude", "Visa"],
            index=0,
            help="Use None when unknown or cross-domain.",
        )
        subject = st.text_input("Subject")
        issue = st.text_area("Issue", height=180, placeholder="Paste full support ticket body here...")
        submitted = st.form_submit_button("Run Triage", use_container_width=True)

    if submitted:
        ticket = TicketInput(issue=issue.strip(), subject=subject.strip(), company=_normalize_company(company))
        decision = triage_ticket(ticket, index)
        _render_decision(asdict(decision))


def render_batch(index: CorpusIndex) -> None:
    st.subheader("Batch Triage (CSV)")
    st.caption("Upload CSV with columns: `Issue`, `Subject`, `Company`.")

    template_csv = "Issue,Subject,Company\nExample issue,Example subject,HackerRank\n"
    st.download_button(
        "Download CSV Template",
        template_csv.encode("utf-8"),
        file_name="ticket_template.csv",
        mime="text/csv",
    )

    uploaded = st.file_uploader("Upload support_tickets.csv", type=["csv"])
    if not uploaded:
        return

    try:
        tickets = _parse_uploaded_csv(uploaded.getvalue())
    except Exception as exc:
        st.error(f"Could not parse CSV: {exc}")
        return

    if not tickets:
        st.warning("No rows found in the uploaded CSV.")
        return

    decisions: List[Dict[str, str]] = []
    progress = st.progress(0.0, text="Running triage...")
    total = len(tickets)
    for i, ticket in enumerate(tickets, start=1):
        decision = triage_ticket(ticket, index)
        decisions.append(
            {
                "issue": ticket.issue,
                "subject": ticket.subject,
                "company": ticket.company,
                "response": decision.response,
                "product_area": decision.product_area,
                "status": decision.status,
                "request_type": decision.request_type,
                "justification": decision.justification,
            }
        )
        progress.progress(i / total, text=f"Processed {i}/{total} tickets")

    st.success(f"Completed triage for {total} tickets.")
    st.markdown("### Output Preview")
    st.markdown("<span style='font-weight:600; font-size:16px;'>Downloaded CSV columns:</span>", unsafe_allow_html=True)
    st.write(
        "The downloaded file includes the full input columns plus the triage output columns in the order shown below. CSV files are plain text, so styling is applied in the app preview only."
    )
    preview_df = [
        {
            "Issue": row["issue"],
            "Subject": row["subject"],
            "Company": row["company"],
            "Response": row["response"],
            "Product Area": row["product_area"],
            "Status": row["status"],
            "Request Type": row["request_type"],
            "Justification": row["justification"],
        }
        for row in decisions
    ]
    st.dataframe(preview_df, use_container_width=True, hide_index=True)

    output_bytes = _rows_to_csv(decisions)
    st.markdown("### Download CSV")
    st.download_button(
        "Download output.csv",
        output_bytes,
        file_name="output.csv",
        mime="text/csv",
        use_container_width=True,
    )


def render_about(data_dir: str) -> None:
    st.subheader("About this app")
    st.markdown(
        "- Uses only local corpus under `data/`\n"
        "- No external web retrieval\n"
        "- Safe escalation for high-risk/sensitive unsupported requests\n"
        "- Output schema: `status`, `product_area`, `response`, `justification`, `request_type`"
    )
    st.caption(f"Corpus path: {Path(data_dir).resolve()}")


def main() -> None:
    st.title("Support Triage Agent")
    st.caption("Browser UI for HackerRank, Claude, and Visa support ticket routing.")

    with st.sidebar:
        st.header("Configuration")
        data_dir_options = _find_data_directories()
        if data_dir_options:
            data_dir = st.selectbox(
                "Data directory",
                options=data_dir_options,
                index=0,
                help="Choose a local corpus folder to load from the repository.",
            )
        else:
            data_dir = st.text_input("Data directory", value="data")
        st.info("Tip: Choose one of the available corpus folders under the repository.")

    try:
        index = get_index(data_dir)
    except Exception as exc:
        st.error(f"Failed to load corpus index from '{data_dir}': {exc}")
        st.stop()

    tab_single, tab_batch, tab_about = st.tabs(["Single Ticket", "Batch CSV", "About"])
    with tab_single:
        render_single_ticket(index)
    with tab_batch:
        render_batch(index)
    with tab_about:
        render_about(data_dir)


if __name__ == "__main__":
    main()
