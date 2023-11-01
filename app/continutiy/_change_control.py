class ChangeControlRecord:
    def __init__(self, request_number, request_date, requested_by, description, justification, impact_assessment, priority, category, implementation_datetime, approver):
        self.request_number = request_number
        self.request_date = request_date
        self.requested_by = requested_by
        self.description = description
        self.justification = justification
        self.impact_assessment = impact_assessment
        self.priority = priority
        self.category = category
        self.implementation_datetime = implementation_datetime
        self.approver = approver
        self.document_info = None
        self.implementation_plan = None
        self.communication_info = None
        self.risk_assessment = None
        self.document_references = None

    def add_document_info(self, doc_info):
        self.document_info = doc_info

    def add_implementation_plan(self, impl_plan):
        self.implementation_plan = impl_plan

    def add_communication_info(self, comm_info):
        self.communication_info = comm_info

    def add_risk_assessment(self, risk_assessment):
        self.risk_assessment = risk_assessment

    def add_document_references(self, doc_references):
        self.document_references = doc_references

    def display_info(self):
        print("Change Control Record:")
        print(f"Change Request Number: {self.request_number}")
        print(f"Change Request Date: {self.request_date}")
        print(f"Requested by: {self.requested_by}")
        print(f"Change Description: {self.description}")
        print(f"Justification for Change: {self.justification}")
        print(f"Impact Assessment: {self.impact_assessment}")
        print(f"Priority: {self.priority}")
        print(f"Category: {self.category}")
        print(f"Implementation Date/Time: {self.implementation_datetime}")
        print(f"Change Approver: {self.approver}")
        if self.document_info:
            self.document_info.display_info()
        if self.implementation_plan:
            self.implementation_plan.display_info()
        if self.communication_info:
            self.communication_info.display_info()
        if self.risk_assessment:
            self.risk_assessment.display_info()
        if self.document_references:
            self.document_references.display_info()


class DocumentControlInformation:
    def __init__(self, title, number, revision_history, last_revision_date, owner, distribution_list):
        self.title = title
        self.number = number
        self.revision_history = revision_history
        self.last_revision_date = last_revision_date
        self.owner = owner
        self.distribution_list = distribution_list

    def display_info(self):
        print("Document Control Information:")
        print(f"Document Title: {self.title}")
        print(f"Document Number: {self.number}")
        print(f"Revision History: {self.revision_history}")
        print(f"Date of Last Revision: {self.last_revision_date}")
        print(f"Document Owner: {self.owner}")
        print(f"Distribution List: {self.distribution_list}")


class ChangeImplementationPlan:
    def __init__(self, scope, steps, resources, timeline, testing_procedures, rollback_plan):
        self.scope = scope
        self.steps = steps
        self.resources = resources
        self.timeline = timeline
        self.testing_procedures = testing_procedures
        self.rollback_plan = rollback_plan

    def display_info(self):
        print("Change Implementation Plan:")
        print(f"Scope of the Change: {self.scope}")
        print(f"Steps for Implementation: {self.steps}")
        print(f"Resources Required: {self.resources}")
        print(f"Timeline for Each Step: {self.timeline}")
        print(f"Testing and Validation Procedures: {self.testing_procedures}")
        print(f"Rollback Plan: {self.rollback_plan}")


class CommunicationAndNotification:
    def __init__(self, stakeholders, communication_plan, notification_process, training_requirements):
        self.stakeholders = stakeholders
        self.communication_plan = communication_plan
        self.notification_process = notification_process
        self.training_requirements = training_requirements

    def display_info(self):
        print("Communication and Notification:")
        print(f"Stakeholders Affected by the Change: {self.stakeholders}")
        print(f"Communication Plan: {self.communication_plan}")
        print(f"Notification Process for Impacted Parties: {self.notification_process}")
        print(f"Training Requirements for Personnel Involved in the Change: {self.training_requirements}")


class RiskAssessmentAndControl:
    def __init__(self, risk_assessment, potential_risks, mitigation_measures, contingency_plans, monitoring_reporting):
        self.risk_assessment = risk_assessment
        self.potential_risks = potential_risks
        self.mitigation_measures = mitigation_measures
        self.contingency_plans = contingency_plans
        self.monitoring_reporting = monitoring_reporting

    def display_info(self):
        print("Risk Assessment and Control:")
        print(f"Risk Assessment of the Change: {self.risk_assessment}")
        print(f"Identification of Potential Risks and Vulnerabilities: {self.potential_risks}")
        print(f"Risk Mitigation Measures: {self.mitigation_measures}")
        print(f"Contingency Plans for Unforeseen Issues or Failures: {self.contingency_plans}")
        print(f"Monitoring and Reporting Mechanisms During the Change Implementation: {self.monitoring_reporting}")


class DocumentReferences:
    def __init__(self, evidence_and_artifacts, record_keeping_requirements, retention_period):
        self.evidence_and_artifacts = evidence_and_artifacts
        self.record_keeping_requirements = record_keeping_requirements
        self.retention_period = retention_period

    def display_info(self):
        print("Document References:")
        print(f"Documented Evidence and Artifacts: {self.evidence_and_artifacts}")
        print(f"Record Keeping Requirements: {self.record_keeping_requirements}")
        print(f"Retention Period: {self.retention_period}")


def create_change_control_record(request_number, request_date, requested_by, description, justification, impact_assessment, priority, category, implementation_datetime, approver):
    return ChangeControlRecord(request_number, request_date, requested_by, description, justification, impact_assessment, priority, category, implementation_datetime, approver)


def create_document_control_information(title, number, revision_history, last_revision_date, owner, distribution_list):
    return DocumentControlInformation(title, number, revision_history, last_revision_date, owner, distribution_list)


def create_change_implementation_plan(scope, steps, resources, timeline, testing_procedures, rollback_plan):
    return ChangeImplementationPlan(scope, steps, resources, timeline, testing_procedures, rollback_plan)


def create_communication_and_notification(stakeholders, communication_plan, notification_process, training_requirements):
    return CommunicationAndNotification(stakeholders, communication_plan, notification_process, training_requirements)


def create_risk_assessment_and_control(risk_assessment, potential_risks, mitigation_measures, contingency_plans, monitoring_reporting):
    return RiskAssessmentAndControl(risk_assessment, potential_risks, mitigation_measures, contingency_plans, monitoring_reporting)


def create_document_references(evidence_and_artifacts, record_keeping_requirements, retention_period):
    return DocumentReferences(evidence_and_artifacts, record_keeping_requirements, retention_period)


def display_combined_info(change_record):
    change_record.display_info()


# Example usage:
if __name__ == "__main__":
    change_info = create_change_control_record(
        request_number="CR-001",
        request_date="2023-10-31",
        requested_by="John Doe - Change Manager",
        description="Update the database schema",
        justification="To improve system performance",
        impact_assessment="Low risk, mitigation in place",
        priority="Medium",
        category="Software",
        implementation_datetime="2023-11-15 08:00 AM",
        approver="Jane Smith - IT Director"
    )

    document_info = create_document_control_information(
        title="Sample Document",
        number="DOC-001",
        revision_history="1.0 Initial Release",
        last_revision_date="2023-10-31",
        owner="John Doe",
        distribution_list="Team A, Team B, Team C"
    )

    implementation_plan = create_change_implementation_plan(
        scope="Update database schema",
        steps="1. Backup database, 2. Apply schema changes, 3. Test changes",
        resources="DBA team, Testing team",
        timeline="2 days",
        testing_procedures="Verify data integrity, performance testing",
        rollback_plan="Restore the previous schema"
    )

    communication_info = create_communication_and_notification(
        stakeholders="IT department, Business stakeholders",
        communication_plan="Email notifications, team meetings",
        notification_process="Notify impacted parties, provide updates",
        training_requirements="Training sessions for DBA team"
    )

    risk_assessment_info = create_risk_assessment_and_control(
        risk_assessment="Low risk",
        potential_risks="Data loss, system downtime",
        mitigation_measures="Regular backups, rollback plan",
        contingency_plans="Data recovery procedures, communication plan",
        monitoring_reporting="Regular progress reports, incident reporting"
    )

    doc_references = create_document_references(
        evidence_and_artifacts="Change documentation, test reports",
        record_keeping_requirements="5 years",
        retention_period="5 years"
    )

    change_info.add_document_info(document_info)
    change_info.add_implementation_plan(implementation_plan)
    change_info.add_communication_info(communication_info)
    change_info.add_risk_assessment(risk_assessment_info)
    change_info.add_document_references(doc_references)

    display_combined_info(change_info)
