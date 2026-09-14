function myFunction() {
  createCop31AntalyaPledgesForm();
}

function createCop31AntalyaPledgesForm() {
  var form = FormApp.create('Submit an indicative commitment to the 2026 Antalya Pledges on AI');
  form.setDescription(
    'Building on the COP29 Declaration on Green Digital Action, a High-Level Green Digital Action Roundtable on Artificial Intelligence will be held on 16 November 2026 during COP31 in Antalya.\n\n' +
    'Please use this form to provide an initial indication of your proposed commitment. Complete only the commitments relevant to your organization.'
  );
  form.setConfirmationMessage('Thank you. Your indicative commitment has been submitted.');

  addSection(form, 'Section 1 - Organization Information', "Please provide your organization's contact details.");
  addText(form, 'Organization Name', true);
  addText(form, 'Organization Type', true);
  addText(form, 'Country / Sector', true);
  addText(form, 'Contact Person', true);
  addText(form, 'Email Address', true);

  form.addSectionHeaderItem()
    .setTitle('Important')
    .setHelpText('For each selected pledge, provide the exact target or number you commit to achieving. Any pledge you do not wish to make should be answered No.');

  var sections = [
    ['Section 2 - A. Measurement, Transparency and Accountability', [
      ['A1', 'Assess the environmental impacts of AI systems and share implementation results and data.', 'Conduct [X] assessments of AI environmental footprint using internationally standardized methodologies by [X].', 'Conduct 20 assessments of AI environmental footprint using internationally standardized methodologies by 2030.'],
      ['A2', 'Measure and share national ICT sector greenhouse gas emissions using internationally harmonized indicators.', 'ICT GHG inventory produced and publicly reported by [X].', 'ICT GHG inventory produced and publicly reported by 2028.'],
      ['A3', 'Publicly disclose Scope 1, Scope 2 and Scope 3 greenhouse gas emissions using recognized reporting frameworks.', 'Public disclosure of Scope 1, Scope 2 and Scope 3 greenhouse gas emissions beginning in [X].', 'Public disclosure of Scope 1, Scope 2 and Scope 3 greenhouse gas emissions beginning in 2028 using a recognized reporting framework.']
    ]],
    ['Section 3 - B. Infrastructure', [
      ['B1', 'Increase the percentage of AI infrastructure powered by renewable energy.', '[X]% of AI infrastructure powered by renewable energy by [X].', '80% of AI infrastructure powered by renewable energy by 2030.'],
      ['B2', 'Adopt green data centre procurement requirements.', 'Green data centre requirements to be formally integrated into procurement processes by [X].', 'Green data centre requirements formally integrated into procurement processes by 2028.'],
      ['B3', 'Integrate sustainability by design in data centre development, construction and operation.', 'Adopt guidelines on the selection and measurement of cooling technologies for data centres by [X].', 'Guidelines on the selection and measurement of cooling technologies adopted by 2028.']
    ]],
    ['Section 4 - C. Design', [
      ['C1', 'Assess sustainability considerations when selecting, developing or deploying AI systems.', 'Guidelines or procurement requirements for green AI model design to be formally adopted by [X]. [X] of AI models applying green AI model design criteria by [X].', 'Green AI model design guidelines formally adopted by 2028. 80% of AI models applying green AI design criteria by 2030.']
    ]],
    ['Section 5 - D. AI Circularity and E-waste', [
      ['D1', 'Adopt guidelines or procurement requirements for circularity, responsible decommissioning, reuse, recycling and e-waste management.', 'Guidelines or procurement requirements to be formally adopted by [X].', 'Circularity and e-waste management guidelines formally adopted by 2028.'],
      ['D2', 'Adopt circular design approaches that promote the efficient use, recovery and reuse of materials used in AI infrastructure and hardware.', '[X] of AI projects applying circularity criteria by [X].', '50% of AI projects applying circularity criteria by 2028.']
    ]],
    ['Section 6 - E. AI for Climate Action', [
      ['E1', 'Mobilize and provide financial, technical and other resources to support the development, deployment and scaling of inclusive AI solutions for climate action.', 'Financial, in-kind or technical support valued at [CHF] committed to benefit [X] countries and/or stakeholders by [X].', 'CHF 2 million in technical assistance committed to support 10 countries by 2030.'],
      ['E2', 'Provide training on sustainable AI for AI developers, policymakers and other relevant stakeholders.', '[X] trained stakeholders by [X].', '1000 AI developers and policymakers trained on sustainable AI by 2028.'],
      ['E3', 'Assess the environmental impact and emissions-reduction potential of digital technologies across sectors and share implementation results and data.', '[X] assessments on the environmental impacts and emissions-reduction potential of digital technologies across sectors conducted by [X].', '10 assessments of digital technologies across the energy, transport and agriculture sectors completed by 2028.']
    ]]
  ];

  sections.forEach(function(section) {
    addSection(form, section[0], 'Select Yes only for commitments your organization intends to make. Then provide the target in the following question.');
    section[1].forEach(function(pledge) {
      addMultipleChoice(form, pledge[0] + '. Do you intend to make this commitment?', ['Yes', 'No'], false);
      addText(form, pledge[0] + '. Target / Deliverable: ' + pledge[2] + '\nExample: ' + pledge[3], false);
    });
  });

  addSection(form, 'Section 7 - Submission and Consent', 'Please review the information provided and indicate whether your commitment(s) may be publicly communicated.');
  addMultipleChoice(form, 'May this pledge be publicly communicated by the COP31 Presidency, ITU, UNFCCC and Green Digital Action?', ['Yes', 'No'], true);

  Logger.log('Edit URL: ' + form.getEditUrl());
  Logger.log('Public URL: ' + form.getPublishedUrl());
}

function addSection(form, title, helpText) {
  form.addPageBreakItem().setTitle(title).setHelpText(helpText);
}

function addText(form, title, required) {
  form.addTextItem().setTitle(title).setRequired(required);
}

function addMultipleChoice(form, title, choices, required) {
  form.addMultipleChoiceItem().setTitle(title).setChoiceValues(choices).setRequired(required);
}