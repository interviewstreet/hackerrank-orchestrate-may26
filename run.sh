#!/bin/bash
# ============================================================
#  HackerRank Orchestrate — Support Triage Agent (Unix/macOS)
# ============================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}[Setup]${NC} HackerRank Orchestrate — Support Triage Agent"
echo ""

# Check for .env
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo -e "${YELLOW}[WARNING]${NC} .env not found"
    echo "  cp .env.example .env && nano .env"
    echo ""
fi

# Install dependencies
echo -e "${GREEN}[Setup]${NC} Installing dependencies..."
pip install -q -r requirements.txt
echo -e "${GREEN}[OK]${NC} Dependencies installed"
echo ""

# Run the agent
echo -e "${GREEN}[Run]${NC} Processing support_tickets.csv..."
echo ""
cd code
python main.py --file ../support_tickets/support_tickets.csv --output ../support_tickets/output.csv
cd ..

echo ""
echo -e "${GREEN}[Done]${NC} Results written to support_tickets/output.csv"
echo ""
