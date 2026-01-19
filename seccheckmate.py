#!/usr/bin/env python3
"""
SecCheckmate - Professional Security Assessment Tool
Industry-standard security checklist and reporting platform for 2026+

Usage:
    python seccheckmate.py              # Interactive mode
    python seccheckmate.py --quick      # Quick mode (minimal prompts)
    python seccheckmate.py --batch      # Batch mode with all tests

Author: Security Community
License: MIT
"""

import yaml
import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Configuration
CHECKLIST_DIR = "checklists"
REPORT_DIR = "reports"
CONFIG_FILE = "config/settings.yaml"
VERSION = "1.0.0"


class SecCheckmate:
    """
    Professional Security Assessment Framework.
    Industry-standard tool for comprehensive security assessments.
    """

    def __init__(self):
        """Initialize the application."""
        self.checklist_dir = Path(CHECKLIST_DIR)
        self.report_dir = Path(REPORT_DIR)
        self.config = self._load_config()
        self._ensure_directories()
        self.current_checklist = None
        self.current_results = []

    def _ensure_directories(self) -> None:
        """Ensure all required directories exist."""
        self.checklist_dir.mkdir(exist_ok=True)
        self.report_dir.mkdir(exist_ok=True)

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from settings file."""
        config_path = Path(CONFIG_FILE)
        if config_path.exists():
            try:
                with open(config_path, "r") as f:
                    return yaml.safe_load(f) or {}
            except Exception:
                pass
        return {
            "organization": "Your Organization",
            "version": VERSION,
            "tool": {"name": "SecCheckmate"}
        }

    def list_checklists(self) -> List[str]:
        """List all available checklists."""
        if not self.checklist_dir.exists():
            return []
        return sorted([f.stem for f in self.checklist_dir.glob("*.yaml")])

    def load_checklist(self, name: str) -> Optional[Dict[str, Any]]:
        """Load a checklist from file."""
        filepath = self.checklist_dir / f"{name}.yaml"
        if not filepath.exists():
            return None
        try:
            with open(filepath, "r") as f:
                return yaml.safe_load(f)
        except yaml.YAMLError:
            return None

    def run_checklist(self, checklist: Dict[str, Any], mode: str = "interactive") -> List[Dict[str, Any]]:
        """Run checklist with specified mode."""
        results = []
        tests = checklist.get("tests", [])
        total = len(tests)

        self._print_header(f"Assessment: {checklist.get('category', 'Unknown')}")
        print(f"Total Tests: {total}\n")

        try:
            for idx, test in enumerate(tests, 1):
                self._display_test(test, idx, total)
                status, notes = self._get_test_input(mode)
                
                results.append({
                    "id": test["id"],
                    "title": test["title"],
                    "description": test.get("description", ""),
                    "severity": test["severity"],
                    "status": status,
                    "notes": notes,
                    "category": test.get("category", "General")
                })
                
                # Show progress
                if idx % 10 == 0:
                    self._show_progress(idx, total)
        
        except KeyboardInterrupt:
            # User interrupted - save partial results
            print("\n\n⚠️  Assessment interrupted by user!")
            print(f"✅ Completed: {len(results)}/{total} tests")
            print("📋 Generating report with completed tests...\n")
            # Results will be saved even though incomplete

        self.current_results = results
        self.current_checklist = checklist
        return results

    def _display_test(self, test: Dict[str, Any], current: int, total: int) -> None:
        """Display a test with professional formatting."""
        severity_emoji = self._get_severity_emoji(test["severity"])
        
        # Compact display for long checklists
        if total > 20:
            print(f"\n[{current:3d}/{total}] {severity_emoji} {test['id']:12s} {test['title'][:55]}")
        else:
            print(f"\n[{current}/{total}] {severity_emoji} [{test['id']}] {test['title']}")
            print(f"    📝 {test.get('description', 'N/A')[:70]}")
            print(f"    ⚠️  Severity: {test['severity']}")

    def _show_progress(self, current: int, total: int) -> None:
        """Show progress bar."""
        percent = (current / total) * 100
        bar_length = 40
        filled = int(bar_length * current / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"    Progress: {bar} {percent:.0f}%")

    @staticmethod
    def _get_severity_emoji(severity: str) -> str:
        """Get emoji for severity level."""
        severity_map = {
            "Critical": "🔴",
            "High": "🟠",
            "Medium": "🟡",
            "Low": "🟢",
            "Info": "🔵"
        }
        return severity_map.get(severity, "⚪")

    def _get_test_input(self, mode: str = "interactive") -> Tuple[str, str]:
        """Get user input for test result with improved UX."""
        valid_statuses = {
            'p': 'PASS',
            'y': 'PASS',
            'yes': 'PASS',
            'pass': 'PASS',
            'f': 'FAIL',
            'n': 'FAIL',
            'no': 'FAIL',
            'fail': 'FAIL',
            'na': 'NA',
            'n/a': 'NA',
            'not applicable': 'NA',
            '': 'NA'  # Empty input = N/A (makes it faster!)
        }

        while True:
            try:
                if mode == "interactive":
                    prompt = "    Status [p/y=PASS, f/n=FAIL, na=N/A, ENTER=N/A, or Ctrl+C]: "
                else:
                    prompt = "    Status [p/f/na/ENTER]: "
                
                user_input = input(prompt).lower().strip()
                
                if user_input in valid_statuses:
                    status = valid_statuses[user_input]
                    break
                else:
                    print("    ❌ Invalid input. Use: p (PASS), f (FAIL), na (N/A), or just press ENTER for N/A")
                    continue
                
            except KeyboardInterrupt:
                # User interrupted - raise to be caught by run_checklist
                raise KeyboardInterrupt("User interrupted assessment")

        # Get evidence notes
        if mode == "interactive":
            notes = input("    📋 Evidence/Notes (optional, press Enter to skip): ").strip()
        else:
            notes = ""

        return status, notes

    def generate_report(self, category: str, results: List[Dict[str, Any]]) -> str:
        """Generate professional report."""
        self.report_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.report_dir / f"report_{timestamp}.md"

        stats = self._calculate_stats(results)
        content = self._build_report_content(category, results, stats, timestamp)

        with open(filename, "w") as f:
            f.write(content)

        return str(filename)

    @staticmethod
    def _calculate_stats(results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate comprehensive statistics."""
        total = len(results)
        passed = sum(1 for r in results if r["status"] == "PASS")
        failed = sum(1 for r in results if r["status"] == "FAIL")
        na = sum(1 for r in results if r["status"] == "NA")

        critical_failed = sum(1 for r in results if r["severity"] == "Critical" and r["status"] == "FAIL")
        high_failed = sum(1 for r in results if r["severity"] == "High" and r["status"] == "FAIL")

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "na": na,
            "pass_rate": (passed / total * 100) if total > 0 else 0,
            "critical_failed": critical_failed,
            "high_failed": high_failed
        }

    def _build_report_content(self, category: str, results: List[Dict[str, Any]], 
                            stats: Dict[str, Any], timestamp: str) -> str:
        """Build comprehensive report content."""
        org_name = self.config.get("organization", {})
        if isinstance(org_name, dict):
            org_name = org_name.get("name", "Your Organization")

        lines = [
            "# 🛡️ Security Assessment Report",
            "",
            f"**Assessment Category:** {category}",
            f"**Organization:** {org_name}",
            f"**Assessment Date:** {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}",
            f"**Report ID:** {timestamp}",
            f"**Tool:** SecCheckmate v{VERSION}",
            "",
            "---",
            "",
            "## 📊 Executive Summary",
            "",
            f"This assessment evaluated **{stats['total']} security controls** across {category}.",
            "",
            "### Key Metrics",
            "",
            "| Metric | Count | Percentage | Status |",
            "|--------|-------|-----------|--------|",
            f"| ✅ Passed | {stats['passed']} | {stats['pass_rate']:.1f}% | Good |",
            f"| ❌ Failed | {stats['failed']} | {(stats['failed']/stats['total']*100) if stats['total'] > 0 else 0:.1f}% | {'Critical' if stats['failed'] > 0 else 'N/A'} |",
            f"| ⏭️ Not Applicable | {stats['na']} | {(stats['na']/stats['total']*100) if stats['total'] > 0 else 0:.1f}% | N/A |",
            "",
        ]

        # Risk Assessment
        if stats['critical_failed'] > 0 or stats['high_failed'] > 0:
            lines.extend([
                "### ⚠️ Risk Assessment",
                "",
                f"- **Critical Issues Found:** {stats['critical_failed']}",
                f"- **High Severity Issues:** {stats['high_failed']}",
                "",
                "> **Action Required:** Immediate remediation needed for critical findings.",
                "",
            ])

        # Findings by Severity
        lines.extend(["## 🔍 Findings by Severity", ""])

        severity_order = ["Critical", "High", "Medium", "Low", "Info"]
        for severity in severity_order:
            severity_results = [r for r in results if r["severity"] == severity]
            if severity_results:
                failed_count = sum(1 for r in severity_results if r["status"] == "FAIL")
                emoji = self._get_severity_emoji(severity)
                
                lines.append(f"### {emoji} {severity} Severity ({failed_count} Failed)")
                lines.append("")
                
                for r in severity_results:
                    if r["status"] == "FAIL":
                        lines.append(f"- **{r['id']}:** {r['title']}")
                
                lines.append("")

        # Detailed Findings
        lines.extend(["## 📋 Detailed Assessment Results", ""])

        for r in results:
            status_symbol = "✅" if r["status"] == "PASS" else "❌" if r["status"] == "FAIL" else "⏭️"
            
            lines.extend([
                f"### {status_symbol} {r['id']} - {r['title']}",
                "",
                f"| Field | Value |",
                f"|-------|-------|",
                f"| Status | {r['status']} |",
                f"| Severity | {r['severity']} |",
                f"| Category | {r.get('category', 'General')} |",
                f"| Description | {r['description'][:100]} |",
                f"| Evidence | {r['notes'] if r['notes'] else 'N/A'} |",
                "",
            ])

        # Recommendations
        lines.extend([
            "---",
            "",
            "## 💡 Recommendations",
            "",
            "1. **Address Critical Issues Immediately** - These require urgent attention",
            "2. **Plan High Priority Remediation** - Create an action plan within 30 days",
            "3. **Schedule Regular Assessments** - Conduct quarterly security reviews",
            "4. **Maintain Documentation** - Keep detailed records of remediation efforts",
            "5. **Review and Update** - Share findings with relevant teams",
            "",
            "---",
            "",
            f"*Report generated by **SecCheckmate v{VERSION}** | Industry-Standard Security Assessment Tool*",
            f"*For more information, visit: https://github.com/yourusername/seccheckmate*",
        ])

        return "\n".join(lines)

    def _print_header(self, title: str) -> None:
        """Print formatted header."""
        print("\n" + "=" * 70)
        print(f"  {title}")
        print("=" * 70)

    def display_main_menu(self) -> None:
        """Display main menu with professional formatting."""
        print("\n" + "=" * 70)
        print("  🛡️  SecCheckmate - Professional Security Assessment Framework")
        print(f"  Version {VERSION} | Industry Standard for 2026+")
        print("=" * 70)
        print("\nOptions:")
        print("  1. 🚀 Run Security Assessment")
        print("  2. 📚 View Available Assessments")
        print("  3. 📊 View Recent Reports")
        print("  4. ⚙️  Settings")
        print("  5. ❌ Exit")
        print("-" * 70)

    def interactive_mode(self) -> None:
        """Main interactive loop."""
        while True:
            self.display_main_menu()
            choice = input("Select option (1-5): ").strip()

            if choice == "1":
                self._run_assessment()
            elif choice == "2":
                self._view_assessments()
            elif choice == "3":
                self._view_reports()
            elif choice == "4":
                self._show_settings()
            elif choice == "5":
                self._exit_app()
                break
            else:
                print("❌ Invalid choice. Please select 1-5.")

    def _run_assessment(self) -> None:
        """Run assessment workflow."""
        checklists = self.list_checklists()
        if not checklists:
            print("\n❌ No assessments found.")
            return

        self._print_header("Available Security Assessments")
        for idx, name in enumerate(checklists, 1):
            print(f"  {idx}. {name}")

        try:
            choice = int(input(f"\nSelect assessment (1-{len(checklists)}): "))
            if 1 <= choice <= len(checklists):
                checklist = self.load_checklist(checklists[choice - 1])
                if checklist:
                    test_count = len(checklist.get("tests", []))
                    
                    # Mode selection for long checklists
                    if test_count > 30:
                        print(f"\n📌 This assessment has {test_count} tests.")
                        print("Select mode:")
                        print("  1. Interactive (detailed, with evidence capture)")
                        print("  2. Quick (minimal prompts)")
                        mode_choice = input("Select mode (1-2) [default: 1]: ").strip()
                        mode = "quick" if mode_choice == "2" else "interactive"
                    else:
                        mode = "interactive"

                    results = self.run_checklist(checklist, mode)
                    report_path = self.generate_report(checklist["category"], results)
                    
                    self._print_header("Assessment Complete ✅")
                    pass_rate = (sum(1 for r in results if r["status"] == "PASS") / len(results) * 100)
                    print(f"Pass Rate: {pass_rate:.1f}%")
                    print(f"Report saved: {report_path}")
        except ValueError:
            print("❌ Invalid input.")

    def _view_assessments(self) -> None:
        """View detailed assessment information."""
        checklists = self.list_checklists()
        if not checklists:
            print("\n❌ No assessments available.")
            return

        self._print_header("Assessment Catalog")
        for name in checklists:
            checklist = self.load_checklist(name)
            if checklist:
                test_count = len(checklist.get("tests", []))
                desc = checklist.get("description", "N/A")
                print(f"\n📋 {name.upper()}")
                print(f"   Category: {checklist.get('category', 'N/A')}")
                print(f"   Tests: {test_count}")
                print(f"   Description: {desc[:70]}")

    def _view_reports(self) -> None:
        """View recent reports."""
        reports = list(self.report_dir.glob("*.md"))
        if not reports:
            print("\n❌ No reports generated yet.")
            return

        self._print_header("Recent Reports")
        reports.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        for idx, report in enumerate(reports[:10], 1):
            size_kb = report.stat().st_size / 1024
            print(f"  {idx}. {report.name} ({size_kb:.1f} KB)")

    def _show_settings(self) -> None:
        """Show current settings."""
        self._print_header("Settings")
        print(f"Organization: {self.config.get('organization', 'N/A')}")
        print(f"Tool Version: {VERSION}")
        print(f"Reports Directory: {self.report_dir}")
        print(f"Checklists Directory: {self.checklist_dir}")

    @staticmethod
    def _exit_app() -> None:
        """Exit with goodbye message."""
        print("\n" + "=" * 70)
        print("  👋 Thank you for using SecCheckmate!")
        print("  🌟 Star us on GitHub: https://github.com/yourusername/seccheckmate")
        print("  📧 Questions? Open an issue on GitHub")
        print("=" * 70 + "\n")


def main() -> None:
    """Main entry point."""
    try:
        app = SecCheckmate()
        app.interactive_mode()
    except KeyboardInterrupt:
        print("\n\n⚠️  Assessment interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
