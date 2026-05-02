#!/usr/bin/env python3
"""
analyze_results.py — Post-run statistics and visualization for output.csv.

Generates premium, high-fidelity charts showing:
  - Status distribution (replied vs escalated)
  - Domain (product_area) breakdown
  - Request type distribution
  - Escalation breakdown by domain
"""

import argparse
import os
import sys
from pathlib import Path

import pandas as pd

# Try to import matplotlib for chart generation
try:
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


# ---------------------------------------------------------------------------
# Color palette — premium, high-contrast
# ---------------------------------------------------------------------------

COLORS = {
    "replied":      "#00F5D4",   # Neon Teal
    "escalated":    "#FF006E",   # Electric Magenta
    "hackerrank":   "#3A86FF",   # Bright Blue
    "claude":       "#8338EC",   # Deep Violet
    "visa":         "#FFBE0B",   # Vivid Amber
    "unknown":      "#8D99AE",   # Slate Gray
    "product_issue":"#3A86FF",   # Re-use Bright Blue
    "feature_request":"#FB5607", # Bold Orange
    "bug":          "#FF006E",   # Re-use Magenta
    "invalid":      "#5D2E46",   # Dark Plum
}


def print_separator(char: str = "─", width: int = 60) -> None:
    """Print a styled separator line."""
    print(f"\033[90m{char * width}\033[0m")


def print_header(title: str) -> None:
    """Print a styled section header."""
    print_separator()
    print(f"\033[1;36m  {title}\033[0m")
    print_separator()


def print_stat(label: str, value: str, color: str = "\033[97m") -> None:
    """Print a single key-value stat line."""
    print(f"  \033[90m{label:<30}\033[0m {color}{value}\033[0m")


def analyze(df: pd.DataFrame) -> dict:
    """Compute all statistics from the output DataFrame."""
    stats = {}
    stats["total"] = len(df)

    # Normalize columns
    status_col = "action" if "action" in df.columns else "status"
    df["status_norm"] = df[status_col].str.strip().str.lower() if status_col in df.columns else "unknown"

    if "product_area" in df.columns:
        # Extract primary domain — split by ' - ' as used in main.py
        df["domain"] = df["product_area"].str.split(" - ").str[0].str.strip().str.lower()
    else:
        df["domain"] = "unknown"

    if "request_type" in df.columns:
        df["request_type_norm"] = df["request_type"].str.strip().str.lower()
    else:
        df["request_type_norm"] = "unknown"

    stats["status_counts"]       = df["status_norm"].value_counts()
    stats["domain_counts"]       = df["domain"].value_counts()
    stats["request_type_counts"] = df["request_type_norm"].value_counts()

    # Escalation breakdown per domain
    escalated = df[df["status_norm"] == "escalated"]
    stats["escalation_by_domain"] = escalated["domain"].value_counts()

    total = stats["total"]
    replied   = stats["status_counts"].get("replied",   0)
    escalated_count = stats["status_counts"].get("escalated", 0)

    stats["reply_rate"]      = (replied / total * 100) if total > 0 else 0
    stats["escalation_rate"] = (escalated_count / total * 100) if total > 0 else 0

    return stats


def print_terminal_report(stats: dict) -> None:
    """Print a richly formatted terminal statistics report."""
    print()
    print_header("SUPPORT TRIAGE AGENT — RUN REPORT")

    print(f"\n  \033[1mTotal Tickets Processed:\033[0m  \033[1;97m{stats['total']}\033[0m\n")

    print_header("Status Distribution")
    for status, count in stats["status_counts"].items():
        pct = count / stats["total"] * 100
        bar = "█" * int(pct / 3)
        color = "\033[92m" if status == "replied" else "\033[91m"
        print(f"  {color}{status:<12}\033[0m {count:>3}  ({pct:5.1f}%)  {color}{bar}\033[0m")

    print()
    print_header("Domain (Product Area) Breakdown")
    for domain, count in stats["domain_counts"].items():
        pct = count / stats["total"] * 100
        bar = "█" * int(pct / 2)
        print(f"  \033[93m{domain:<20}\033[0m {count:>3}  ({pct:5.1f}%)  \033[93m{bar}\033[0m")

    print()
    print_header("Request Type Distribution")
    for rtype, count in stats["request_type_counts"].items():
        pct = count / stats["total"] * 100
        bar = "█" * int(pct / 2)
        print(f"  \033[94m{rtype:<22}\033[0m {count:>3}  ({pct:5.1f}%)  \033[94m{bar}\033[0m")

    print()
    print_header("Escalation Breakdown by Domain")
    if len(stats["escalation_by_domain"]) > 0:
        for domain, count in stats["escalation_by_domain"].items():
            print(f"  \033[91m{domain:<20}\033[0m {count:>3} escalated")
    else:
        print("  \033[92mNo escalations recorded.\033[0m")

    print()
    print_header("Summary")
    print_stat("Reply Rate:",      f"{stats['reply_rate']:.1f}%",      "\033[92m")
    print_stat("Escalation Rate:", f"{stats['escalation_rate']:.1f}%", "\033[91m")
    print_separator()
    print()


def save_charts(stats: dict, output_dir: Path) -> None:
    """Generate premium PNG charts summarizing agent performance."""
    if not HAS_MATPLOTLIB:
        print("  [!] matplotlib not installed. Skipping chart generation.")
        return

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Global Plot Settings
    plt.rcParams["font.family"] = "sans-serif"
    
    BG_COLOR = "#0F172A"  # Dark Slate Blue
    PAPER_COLOR = "#1E293B" # Slightly Lighter Slate

    # ── Chart 1: Status Distribution (Donut) ────────────────────────────────
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    status_data   = stats["status_counts"]
    status_colors = [COLORS.get(k, "#95A5A6") for k in status_data.index]
    
    wedges, texts, autotexts = ax.pie(
        status_data.values,
        labels=status_data.index.str.upper(),
        colors=status_colors,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.85,
        explode=[0.05] * len(status_data),
        textprops={"color": "white", "fontsize": 14, "fontweight": "bold"}
    )
    centre_circle = plt.Circle((0,0), 0.70, fc=BG_COLOR)
    fig.gca().add_artist(centre_circle)

    ax.set_title("AUTOMATION STATUS\nReplied vs Escalated",
                 color="white", fontsize=20, fontweight="bold", pad=20)
    plt.tight_layout()
    chart_path = output_dir / "status_distribution.png"
    plt.savefig(chart_path, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"  ✅  Saved: {chart_path}")

    # ── Chart 2: Domain Breakdown (Horizontal Bar) ───────────────────────────
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(PAPER_COLOR)

    domain_data   = stats["domain_counts"]
    domain_colors = [COLORS.get(k, "#95A5A6") for k in domain_data.index]
    bars = ax.barh(domain_data.index.str.upper(), domain_data.values, color=domain_colors, height=0.6)

    ax.grid(axis='x', color='white', linestyle='--', alpha=0.1)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#475569')
    ax.spines['bottom'].set_color('#475569')

    for bar, val in zip(bars, domain_data.values):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f" {val} ", va="center", ha="left", color="white", fontweight="bold", fontsize=12)

    ax.set_xlabel("TICKET COUNT", color="#94A3B8", fontweight="bold")
    ax.set_title("TICKET VOLUME BY DOMAIN", color="white", fontsize=20, fontweight="bold", pad=20)
    ax.tick_params(colors="white", labelsize=12)
    plt.tight_layout()
    chart_path = output_dir / "domain_breakdown.png"
    plt.savefig(chart_path, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"  ✅  Saved: {chart_path}")

    # ── Chart 3: Request Type Breakdown (Horizontal Bar) ─────────────────────
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(PAPER_COLOR)

    rt_data   = stats["request_type_counts"]
    rt_colors = [COLORS.get(k, "#95A5A6") for k in rt_data.index]
    bars = ax.barh(rt_data.index.str.replace('_', ' ').str.upper(), rt_data.values, color=rt_colors, height=0.7)

    ax.grid(axis='x', color='white', linestyle='--', alpha=0.1)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#475569')
    ax.spines['bottom'].set_color('#475569')

    for bar, val in zip(bars, rt_data.values):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                f" {val} ", va="center", ha="left", color="white", fontweight="bold", fontsize=11)

    ax.set_xlabel("TICKET COUNT", color="#94A3B8", fontweight="bold")
    ax.set_title("REQUEST TYPE DISTRIBUTION", color="white", fontsize=20, fontweight="bold", pad=20)
    ax.tick_params(colors="white", labelsize=11)
    plt.tight_layout()
    chart_path = output_dir / "request_type_breakdown.png"
    plt.savefig(chart_path, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"  ✅  Saved: {chart_path}")

    # ── Chart 4: Escalation by Domain (Grouped Bar) ───────────────────────────
    if len(stats["escalation_by_domain"]) > 0:
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor(BG_COLOR)
        ax.set_facecolor(PAPER_COLOR)

        esc_data = stats["escalation_by_domain"]
        esc_colors = [COLORS.get(k, "#95A5A6") for k in esc_data.index]
        bars = ax.bar(esc_data.index.str.upper(), esc_data.values, color=esc_colors, width=0.5)

        ax.grid(axis='y', color='white', linestyle='--', alpha=0.1)
        ax.set_axisbelow(True)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#475569')
        ax.spines['bottom'].set_color('#475569')

        for bar, val in zip(bars, esc_data.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                    str(val), ha="center", color="white", fontweight="bold", fontsize=14)

        ax.set_ylabel("ESCALATIONS", color="#94A3B8", fontweight="bold")
        ax.set_title("HUMAN ESCALATIONS BY DOMAIN", color="white", fontsize=20, fontweight="bold", pad=20)
        ax.tick_params(colors="white", labelsize=12)
        plt.tight_layout()
        chart_path = output_dir / "escalation_by_domain.png"
        plt.savefig(chart_path, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
        plt.close()
        print(f"  ✅  Saved: {chart_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze and visualize support triage agent output."
    )
    parser.add_argument(
        "--input", "-i",
        default="support_tickets/output.csv",
        help="Path to the output CSV file"
    )
    parser.add_argument(
        "--charts-dir", "-c",
        default="results/",
        help="Directory to save chart PNGs"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"\n  \033[91m[ERROR]\033[0m File not found: {input_path}")
        sys.exit(1)

    print(f"\n  Loading: \033[96m{input_path}\033[0m")
    df = pd.read_csv(input_path)
    stats = analyze(df)

    print_terminal_report(stats)
    print_header("Chart Generation")
    save_charts(stats, Path(args.charts_dir))


if __name__ == "__main__":
    main()
