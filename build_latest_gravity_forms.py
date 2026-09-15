import json
from pathlib import Path

OUT = Path(__file__).with_name('cop31_pledges_gravity_forms.json')


def logic(field_id, value):
    return {
        'actionType': 'show',
        'logicType': 'all',
        'rules': [{'fieldId': str(field_id), 'operator': 'is', 'value': value}],
    }


def audience_logic(audience):
    if audience == 'not-government':
        return {
            'actionType': 'show',
            'logicType': 'all',
            'rules': [{'fieldId': '3', 'operator': 'isnot', 'value': 'government'}],
        }
    if audience == 'private-university':
        return {
            'actionType': 'show',
            'logicType': 'any',
            'rules': [
                {'fieldId': '3', 'operator': 'is', 'value': 'private-sector'},
                {'fieldId': '3', 'operator': 'is', 'value': 'university'},
            ],
        }
    return logic(3, audience)


def text_field(field_id, label, css, required=False, number=False, conditional=None):
    field = {
        'id': field_id,
        'type': 'number' if number else 'text',
        'label': label,
        'adminLabel': css,
        'cssClass': css,
        'isRequired': required,
    }
    if conditional:
        field['conditionalLogic'] = conditional
    return field


def pledge_fields(fields, code, label, target, example, audience=None, targets=()):
    checkbox_id = len(fields) + 1
    checkbox = {
        'id': checkbox_id,
        'type': 'checkbox',
        'label': f'{code}. {label}',
        'description': f'Target / Deliverable: {target}\n\nExample: {example}',
        'adminLabel': f'{code} commitment',
        'cssClass': f'pledge-{code.lower().replace(".", "-")}',
        'choices': [{'text': 'I intend to make this commitment', 'value': '1', 'isSelected': False}],
    }
    if audience:
        checkbox['conditionalLogic'] = audience_logic(audience)
    fields.append(checkbox)
    for suffix, field_label, number in targets:
        fields.append(text_field(
            len(fields) + 1,
            field_label,
            f'{code.lower().replace(".", "-")}-{suffix}',
            number=number,
            conditional=logic(checkbox_id, '1'),
        ))


def section(fields, field_id, label, description=''):
    fields.append({'id': field_id, 'type': 'section', 'label': label, 'description': description})


def main():
    fields = []
    section(fields, 1, 'Section 1 - Organization Information', "Please provide your organization's contact details.")
    fields.append(text_field(2, 'Organization Name', 'org-name', required=True))
    fields.append({
        'id': 3, 'type': 'select', 'label': 'Organization Type', 'adminLabel': 'org-type',
        'cssClass': 'org-type', 'isRequired': True,
        'choices': [
            {'text': 'Government', 'value': 'government'},
            {'text': 'Private sector', 'value': 'private-sector'},
            {'text': 'University', 'value': 'university'},
            {'text': 'Civil society organization', 'value': 'civil-society'},
            {'text': 'Other', 'value': 'other'},
        ],
    })
    fields.append(text_field(4, 'Country / Sector', 'country-sector', required=True))
    fields.append(text_field(5, 'Contact Person', 'contact', required=True))
    fields.append({'id': 6, 'type': 'email', 'label': 'Email Address', 'adminLabel': 'email', 'isRequired': True})

    section(fields, 7, 'Section 2 - A. Measurement, Transparency and Accountability', 'Please select the commitments relevant to your organization and complete their targets.')
    pledge_fields(fields, 'A1', 'Assess the environmental impacts of AI systems and share implementation results and data', 'Conduct and publicly disclose [X] assessments of AI environmental impacts using internationally recognized methodologies by [X].', 'Conduct 20 assessments of AI environmental impacts using internationally recognized methodologies by 2030.', targets=(('number', 'Number of assessments', True), ('year', 'Target year', True)))
    pledge_fields(fields, 'A2', 'Measure and share national ICT sector greenhouse gas emissions using internationally harmonized indicators.', 'ICT GHG inventory produced and publicly reported by [X].', 'ICT GHG inventory produced and publicly reported by 2028.', audience='government', targets=(('year', 'Target year', True),))
    pledge_fields(fields, 'A3', 'Publicly disclose Scope 1, Scope 2 and Scope 3 greenhouse gas emissions using recognized reporting frameworks.', 'ICT GHG inventory produced and publicly reported by [X].', 'ICT GHG inventory produced and publicly reported by 2028.', audience='not-government', targets=(('year', 'Starting year', True),))

    section(fields, 8, 'Section 3 - B. Infrastructure', 'Please select the commitments relevant to your organization and complete their targets.')
    pledge_fields(fields, 'B1', 'Increase the percentage of AI infrastructure powered by renewable energy.', '[X]% of AI infrastructure powered by renewable energy by [X].', '80% of AI infrastructure powered by renewable energy by 2030.', targets=(('percent', 'Renewable-energy share (%)', True), ('year', 'Target year', True)))
    pledge_fields(fields, 'B2', 'Adopt green data centre procurement requirements.', 'Green data centre requirements to be formally integrated into procurement processes by [X].', 'Green data centre requirements formally integrated into procurement processes by 2028.', targets=(('year', 'Target year', True),))
    pledge_fields(fields, 'B3.1', 'Integrate sustainability by design in data centre development, construction and operation.', 'Adopt guidelines on the selection and measurement of cooling technologies for data centres by [X].', 'Guidelines on the selection and measurement of cooling technologies adopted by 2028.', targets=(('year', 'Target year', True),))
    pledge_fields(fields, 'B3.2', 'Integrate sustainability by design in data centre development, construction and operation.', '[X] of AI energy-efficient infrastructure based on standardized metrics.', '75% of AI infrastructure meeting standardized energy-efficiency metrics.', targets=(('percent', 'Energy-efficient infrastructure (%)', True), ('year', 'Target year', True)))

    section(fields, 9, 'Section 4 - C. Design', 'Please select the commitments relevant to your organization and complete their targets.')
    pledge_fields(fields, 'C1.1', 'Embed sustainability in model selection, development and procurement.', 'Green AI model design guidelines formally adopted by [X].', 'Green AI model design guidelines formally adopted by 2028.', audience='private-university', targets=(('year', 'Guidelines adopted by', True),))
    pledge_fields(fields, 'C1.2', 'Embed sustainability in model selection, development and procurement.', '[X] of AI models applying green AI model design criteria by [X].', '80% of AI models applying green AI design criteria by 2030.', audience='private-university', targets=(('percent', 'AI models applying criteria (%)', True), ('year', 'Models target year', True)))

    section(fields, 10, 'Section 5 - D. AI Circularity and E-waste', 'Please select the commitments relevant to your organization and complete their targets.')
    pledge_fields(fields, 'D1', 'Adopt guidelines or procurement requirements for circularity, responsible decommissioning, reuse, recycling and e-waste management.', 'Guidelines or procurement requirements to be formally adopted by [X].', 'Circularity and e-waste management guidelines formally adopted by 2028.', targets=(('year', 'Target year', True),))
    pledge_fields(fields, 'D2', 'Adopt circular design approaches that promote the efficient use, recovery and reuse of materials used in AI infrastructure and hardware.', '[X] of AI projects applying circularity criteria by [X].', '50% of AI projects applying circularity criteria by 2028.', audience='private-university', targets=(('percent', 'AI projects applying criteria (%)', True), ('year', 'Target year', True)))

    section(fields, 11, 'Section 6 - E. AI for Climate Action', 'Please select the commitments relevant to your organization and complete their targets.')
    pledge_fields(fields, 'E1', 'Mobilize and provide financial, technical and other resources to support the development, deployment and scaling of inclusive AI solutions for climate action.', 'Financial, in-kind and/or technical support valued at CHF [X] committed to benefit [X] countries and/or stakeholders by [X].', 'CHF 500,000 of financial and technical support committed to benefit [X] countries and/or stakeholders by 2028.', targets=(('amount', 'Committed value (CHF)', True), ('beneficiaries', 'Countries and/or stakeholders', True), ('year', 'Target year', True)))
    pledge_fields(fields, 'E2', 'Provide training on sustainable AI for AI developers, policymakers and other relevant stakeholders.', '[X] trained stakeholders by [X].', '1000 AI developers and policymakers trained on sustainable AI by 2028.', targets=(('number', 'Trained stakeholders', True), ('year', 'Target year', True)))
    pledge_fields(fields, 'E3', 'Assess the environmental impact and emissions-reduction potential of digital technologies across sectors and share implementation results and data.', '[X] assessments on the environmental impacts and emissions-reduction potential of digital technologies across sectors conducted by [X].', '10 assessments of digital technologies across the energy, transport and agriculture sectors completed by 2028.', targets=(('number', 'Assessments', True), ('year', 'Target year', True)))

    section(fields, 12, 'Section 7 - Submission and Consent', 'Please review the information provided and indicate whether your commitment(s) may be publicly communicated.')
    fields.append({'id': 13, 'type': 'radio', 'label': 'May this pledge be publicly communicated by the COP31 Presidency, ITU, UNFCCC and Green Digital Action?', 'isRequired': True, 'choices': [{'text': 'Yes', 'value': 'yes'}, {'text': 'No', 'value': 'no'}]})
    section(fields, 14, 'Section 8 - Partner2Connect', 'We encourage you to submit this pledge on the Partner2Connect platform ahead of COP. https://www.itu.int/partner2connect/')
    fields.append({'id': 15, 'type': 'checkbox', 'label': 'This pledge has been added to P2C', 'choices': [{'text': 'Added to P2C', 'value': 'yes'}]})

    form = {
        'title': 'Submit an indicative commitment to the 2026 Antalya Pledges on AI',
        'description': 'Please complete only the pledge commitments your organization intends to make. For each selected pledge, provide the exact target or number you commit to achieving.',
        'fields': fields,
        'confirmationType': 'message',
        'confirmationMessage': 'Thank you for submitting your commitment to the 2026 Antalya Pledges on AI.',
        'labelPlacement': 'top_label',
        'requiredIndicator': 'asterisk',
    }
    OUT.write_text(json.dumps([form], indent=2), encoding='utf-8')
    print(f'Created {OUT} with {len(fields)} fields')


if __name__ == '__main__':
    main()
