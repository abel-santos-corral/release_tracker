# domain/services/report_generation_service.py
import os
import pandas as pd
from domain.services.data_processing_service import DataProcessingService

class ReportGenerationService:
    def __init__(self):
        # Global variables for the root directory and template paths
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.template_dir = os.path.join(self.root_dir, 'templates')

        self.header_template_path = os.path.join(self.template_dir, 'header_report_template.md')
        self.tickets_template_path = os.path.join(self.template_dir, 'tickets_report_template.md')
        self.components_template_path = os.path.join(self.template_dir, 'component_report_template.md')
        self.empty_components_template_path = os.path.join(self.template_dir, 'empty_components_report_template.md')
        self.estimates_template_path = os.path.join(self.template_dir, 'estimates_report_template.md')
        self.no_estimates_template_path = os.path.join(self.template_dir, 'no_estimates_report_template.md')
        self.main_template_path = os.path.join(self.template_dir, 'report_template.md')
        self.no_progress_template_path = os.path.join(self.template_dir, 'no_progress_report_template.md')
        self.progress_template_path = os.path.join(self.template_dir, 'progress_report_template.md')

    def generate_header(self, df):
        """Generate the header section of the report."""
        fix_version = df['Fix Version/s'].iloc[0]
        with open(self.header_template_path, 'r', encoding='utf-8') as file:
            template = file.read()
        header = template.replace('{{fix_version}}', fix_version)
        return header

    def generate_tickets_section(self, df):
        """Generate the tickets section of the report."""
        tickets_table = df[['Summary', 'Issue key', 'Issue Type', 'Status', 'Assignee', 'Original Estimate', 'Remaining Estimate']].to_markdown(index=False)
        with open(self.tickets_template_path, 'r', encoding='utf-8') as file:
            template = file.read()
        tickets_section = template.replace('{{tickets_table}}', tickets_table)
        return tickets_section

    def generate_components_section(self, df):
        """Generate the components section of the report as a table."""
        data_processing_service = DataProcessingService()
        list_components = data_processing_service.prepare_components_list(df)
        if list_components:
            # Create a Markdown table without numbering
            components_table = "| Module |\n|--------|\n" + "\n".join(f"| {comp} |" for comp in list_components)

            with open(self.components_template_path, 'r', encoding='utf-8') as file:
                template = file.read()
            components_section = template.replace('{{components_table}}', components_table)
        else:
            with open(self.empty_components_template_path, 'r', encoding='utf-8') as file:
                components_section = file.read()

        return components_section



    def generate_estimates_section(self, df):
        """Generate the estimates section of the report."""
        to_estimate_df = df[df['Estimated'] == 'No']
        if not to_estimate_df.empty:
            to_estimate_section = to_estimate_df[['Summary', 'Issue key', 'Issue Type', 'Status', 'Assignee', 'Original Estimate', 'Remaining Estimate']].to_markdown(index=False)
            with open(self.estimates_template_path, 'r', encoding='utf-8') as file:
                template = file.read()
            estimates_section = template.replace('{{to_estimate_section}}', to_estimate_section)
        else:
            with open(self.no_estimates_template_path, 'r', encoding='utf-8') as file:
                estimates_section = file.read()
        return estimates_section

    def format_time(self, hours):
        """Format the time in hours, days, and weeks, omitting zero portions."""
        hours = int(hours)
        if hours < 8:
            return f"{hours}h"
        elif hours < 40:
            days = hours // 8
            remaining_hours = hours % 8
            if remaining_hours == 0:
                return f"{days}d"
            else:
                return f"{days}d {remaining_hours}h"
        else:
            weeks = hours // 40
            remaining_days = (hours % 40) // 8
            remaining_hours = (hours % 40) % 8
            parts = []
            if weeks > 0:
                parts.append(f"{weeks}w")
            if remaining_days > 0:
                parts.append(f"{remaining_days}d")
            if remaining_hours > 0:
                parts.append(f"{remaining_hours}h")
            return " ".join(parts)

    def generate_progress_section(self, df):
        """Generate the progress section of the report."""
        total_estimated = df['Original Estimate'].sum()
        total_remaining = df['Remaining Estimate'].sum()

        if total_estimated == 0:
            with open(self.no_progress_template_path, 'r', encoding='utf-8') as file:
                progress_section = file.read()
        else:
            total_estimated_formatted = self.format_time(total_estimated)
            total_remaining_formatted = self.format_time(total_remaining)
            progress_table = f"- Total estimated= {total_estimated_formatted}\n- Total remaining= {total_remaining_formatted}"

            with open(self.progress_template_path, 'r', encoding='utf-8') as file:
                template = file.read()
            progress_section = template.replace('{{progress_table}}', progress_table)

        return progress_section

    def generate_report(self, df, output_path):
        """Generate the full report by combining all sections."""
        header = self.generate_header(df)
        tickets_section = self.generate_tickets_section(df)
        components_section = self.generate_components_section(df)
        estimates_section = self.generate_estimates_section(df)
        progress_section = self.generate_progress_section(df)

        with open(self.main_template_path, 'r', encoding='utf-8') as file:
            template = file.read()

        report = template.replace('{{header}}', header)
        report = report.replace('{{tickets_section}}', tickets_section)
        report = report.replace('{{components_section}}', components_section)
        report = report.replace('{{estimates_section}}', estimates_section)
        report = report.replace('{{progress_section}}', progress_section)

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(report)
