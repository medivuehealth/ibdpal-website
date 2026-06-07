/**
 * Extended state listings (merged after community-data.js).
 */
(function () {
  if (!window.IBDPAL_COMMUNITY) return;

  function stateEntry(name, chapterName, chapterUrl, phone, resources) {
    return {
      name: name,
      ccfChapter: {
        name: chapterName,
        website: chapterUrl,
        phone: phone || null
      },
      resources: resources
    };
  }

  function ccf(name, url, phone, notes) {
    return {
      name: name,
      type: 'Nonprofit chapter',
      website: url,
      phone: phone || null,
      notes: notes
    };
  }

  function center(name, type, url, phone, notes) {
    return { name: name, type: type, website: url, phone: phone || null, notes: notes };
  }

  var nationalLinks = [
    ccf("Crohn's & Colitis Foundation | Find Support Groups", 'https://www.crohnscolitisfoundation.org/find-a-support-group', null, 'Filter by your state for virtual and in-person meetings.'),
    { name: 'ImproveCareNow | Care Centers', type: 'Pediatric locator', website: 'https://www.improvecarenow.org/care-centers', notes: 'Participating pediatric IBD centers nationwide.' }
  ];

  var extra = {
    CA: stateEntry('California', "Crohn's & Colitis Foundation | Greater Los Angeles / Northern California", 'https://www.crohnscolitisfoundation.org/chapters', '310-481-7500', [
      ccf("Crohn's & Colitis Foundation | Greater Los Angeles Chapter", 'https://www.crohnscolitisfoundation.org/chapters/greaterlosangeles', '310-481-7500', 'Events, education, and support across Southern California.'),
      ccf("Crohn's & Colitis Foundation | Northern California Chapter", 'https://www.crohnscolitisfoundation.org/chapters/northerncalifornia', '415-356-9000', 'Programs in the Bay Area and Northern CA.'),
      center('UCSF Center for Colitis and Crohn\'s Disease', 'Academic IBD center', 'https://www.ucsfhealth.org/conditions/inflammatory-bowel-disease', '415-476-5892', 'Adult and pediatric IBD care; confirm current clinic lines on hospital site.'),
      center('Cedars-Sinai Inflammatory Bowel Disease Program', 'Academic IBD center', 'https://www.cedars-sinai.org/programs/inflammatory-bowel-disease.html', '310-423-4249', 'Multidisciplinary Crohn\'s and colitis care in Los Angeles.')
    ].concat(nationalLinks)),
    NY: stateEntry('New York', "Crohn's & Colitis Foundation | Greater NYC / Upstate", 'https://www.crohnscolitisfoundation.org/chapters', '646-943-6828', [
      ccf("Crohn's & Colitis Foundation | Greater New York Chapter", 'https://www.crohnscolitisfoundation.org/chapters/greaternyc', '646-943-6828', 'Support groups, walks, and education in the NYC metro area.'),
      ccf("Crohn's & Colitis Foundation | Upstate New York Chapter", 'https://www.crohnscolitisfoundation.org/chapters/upstateny', '518-456-1270', 'Programs across upstate regions.'),
      center('Mount Sinai IBD Center', 'Academic IBD center', 'https://www.mountsinai.org/locations/center-inflammatory-bowel', '212-241-8100', 'Adult IBD specialists; verify appointment line on website.')
    ].concat(nationalLinks)),
    TX: stateEntry('Texas', "Crohn's & Colitis Foundation | North & Central Texas / Southern Texas", 'https://www.crohnscolitisfoundation.org/chapters', '972-458-3259', [
      ccf("Crohn's & Colitis Foundation | North and Central Texas Chapter", 'https://www.crohnscolitisfoundation.org/chapters/northcentraltexas', '972-458-3259', 'Dallas–Fort Worth area programs and support.'),
      ccf("Crohn's & Colitis Foundation | Southern Texas Chapter", 'https://www.crohnscolitisfoundation.org/chapters/southerntexas', '713-572-2233', 'Houston-area chapter resources.'),
      center('UT Southwestern IBD Program', 'Academic IBD center', 'https://www.utsouthwestern.edu/departments/internal-medicine/divisions/digestive-liver-diseases/', '214-645-8300', 'Crohn\'s and colitis care; confirm division contact on site.')
    ].concat(nationalLinks)),
    FL: stateEntry('Florida', "Crohn's & Colitis Foundation | Florida chapters", 'https://www.crohnscolitisfoundation.org/chapters', '904-332-0915', [
      ccf("Crohn's & Colitis Foundation | Northeastern Florida Chapter", 'https://www.crohnscolitisfoundation.org/chapters/northeasternflorida', '904-332-0915', 'Jacksonville-area support and events.'),
      ccf("Crohn's & Colitis Foundation | South Florida Chapter", 'https://www.crohnscolitisfoundation.org/chapters/southflorida', '561-218-2929', 'Miami and South Florida programs.'),
      center('Mayo Clinic Florida | IBD', 'Academic IBD center', 'https://www.mayoclinic.org/departments-centers/inflammatory-bowel-disease/overview/ovc-20443159', '904-953-2000', 'Jacksonville campus IBD specialists.')
    ].concat(nationalLinks)),
    OH: stateEntry('Ohio', "Crohn's & Colitis Foundation | Northern Ohio Chapter", 'https://www.crohnscolitisfoundation.org/chapters/northernohio', '216-524-7700', [
      ccf("Crohn's & Colitis Foundation | Northern Ohio Chapter", 'https://www.crohnscolitisfoundation.org/chapters/northernohio', '216-524-7700', 'Cleveland-area education and peer support.'),
      center('Cleveland Clinic Inflammatory Bowel Disease Section', 'Academic IBD center', 'https://my.clevelandclinic.org/departments/digestive/diseases/inflammatory-bowel-disease', '216-444-7000', 'Comprehensive Crohn\'s and colitis program.')
    ].concat(nationalLinks)),
    PA: stateEntry('Pennsylvania', "Crohn's & Colitis Foundation | Philadelphia / Western PA", 'https://www.crohnscolitisfoundation.org/chapters', '215-396-9100', [
      ccf("Crohn's & Colitis Foundation | Philadelphia/Delaware Valley Chapter", 'https://www.crohnscolitisfoundation.org/chapters/philadelphia', '215-396-9100', 'Regional support groups and Take Steps events.'),
      ccf("Crohn's & Colitis Foundation | Western Pennsylvania Chapter", 'https://www.crohnscolitisfoundation.org/chapters/westernpa', '412-823-8272', 'Pittsburgh-area programs.'),
      center('University of Pennsylvania IBD Program', 'Academic IBD center', 'https://www.pennmedicine.org/for-patients-and-visitors/find-a-program-or-service/gastroenterology/inflammatory-bowel-disease', '800-789-7366', 'Penn Medicine IBD care.')
    ].concat(nationalLinks)),
    IL: stateEntry('Illinois', "Crohn's & Colitis Foundation | Illinois Chapter", 'https://www.crohnscolitisfoundation.org/chapters/illinois', '312-627-1476', [
      ccf("Crohn's & Colitis Foundation | Illinois Chapter", 'https://www.crohnscolitisfoundation.org/chapters/illinois', '312-627-1476', 'Chicago and statewide education and support.'),
      center('University of Chicago Medicine IBD Center', 'Academic IBD center', 'https://www.uchicagomedicine.org/conditions-services/inflammatory-bowel-disease-ibd', '773-702-1000', 'Adult and pediatric IBD specialists.')
    ].concat(nationalLinks)),
    GA: stateEntry('Georgia', "Crohn's & Colitis Foundation | Georgia Chapter", 'https://www.crohnscolitisfoundation.org/chapters/georgia', '404-982-0616', [
      ccf("Crohn's & Colitis Foundation | Georgia Chapter", 'https://www.crohnscolitisfoundation.org/chapters/georgia', '404-982-0616', 'Atlanta-based programs serving Georgia.'),
      center('Emory Inflammatory Bowel Disease Program', 'Academic IBD center', 'https://www.emoryhealthcare.org/centers-programs/inflammatory-bowel-disease-program/', '404-778-7777', 'Crohn\'s and colitis care at Emory Healthcare.')
    ].concat(nationalLinks)),
    MI: stateEntry('Michigan', "Crohn's & Colitis Foundation | Michigan Chapter", 'https://www.crohnscolitisfoundation.org/chapters/michigan', '248-737-0900', [
      ccf("Crohn's & Colitis Foundation | Michigan Chapter", 'https://www.crohnscolitisfoundation.org/chapters/michigan', '248-737-0900', 'Support groups and advocacy across Michigan.'),
      center('University of Michigan IBD Program', 'Academic IBD center', 'https://www.uofmhealth.org/conditions-treatments/digestive-health/inflammatory-bowel-disease', '888-229-7408', 'Multidisciplinary IBD clinic.')
    ].concat(nationalLinks)),
    NJ: stateEntry('New Jersey', "Crohn's & Colitis Foundation | New Jersey Chapter", 'https://www.crohnscolitisfoundation.org/chapters/newjersey', '908-588-1744', [
      ccf("Crohn's & Colitis Foundation | New Jersey Chapter", 'https://www.crohnscolitisfoundation.org/chapters/newjersey', '908-588-1744', 'Statewide support groups and education.'),
      center('Robert Wood Johnson IBD Program', 'Academic IBD center', 'https://www.rwjbh.org/treatment-care/gastroenterology/inflammatory-bowel-disease/', '732-235-2465', 'IBD care in New Brunswick area; verify on RWJBarnabas site.')
    ].concat(nationalLinks))
  };

  Object.assign(window.IBDPAL_COMMUNITY.states, extra);
})();
