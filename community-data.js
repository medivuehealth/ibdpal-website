/**
 * IBD community resources by U.S. state (educational directory — verify details with each organization).
 */
window.IBDPAL_COMMUNITY = {
  national: {
    name: 'National resources (all states)',
    resources: [
      {
        name: "Crohn's & Colitis Foundation — IBD Help Center",
        type: 'Support & information',
        website: 'https://www.crohnscolitisfoundation.org/live-full/live-full-ibd-help-center',
        phone: '888-694-8872',
        phoneLabel: '888-MY-GUT-PAIN (888-694-8872)',
        email: 'info@crohnscolitisfoundation.org',
        notes: 'Education, support, and help finding local programs.'
      },
      {
        name: "Crohn's & Colitis Foundation — Find a Chapter",
        type: 'Local chapters',
        website: 'https://www.crohnscolitisfoundation.org/chapters',
        phone: null,
        notes: 'Chapters in every state; programs, events, and volunteer networks.'
      },
      {
        name: "Crohn's & Colitis Foundation — Support Groups",
        type: 'Peer support',
        website: 'https://www.crohnscolitisfoundation.org/find-a-support-group',
        phone: null,
        notes: 'Search in-person and virtual groups by state and community.'
      },
      {
        name: 'GIKids (pediatric IBD)',
        type: 'Pediatric education',
        website: 'https://gikids.org/',
        phone: null,
        notes: 'Resources for children, teens, and families living with IBD.'
      },
      {
        name: 'United Ostomy Associations of America',
        type: 'Ostomy peer support',
        website: 'https://ostomy.org/',
        phone: '800-826-0826',
        notes: 'Support for people with ostomies, including many with IBD.'
      }
    ]
  },
  states: {
    NC: {
      name: 'North Carolina',
      ccfChapter: {
        name: "Crohn's & Colitis Foundation — Carolinas Chapter",
        serves: 'North Carolina & South Carolina',
        website: 'https://www.crohnscolitisfoundation.org/chapters/carolinas',
        contactsUrl: 'https://www.crohnscolitisfoundation.org/chapters/carolinas/contacts',
        phone: '704-264-0587',
        email: 'carolinas@crohnscolitisfoundation.org',
        address: '8508 Park Road #157, Charlotte, NC 28210'
      },
      resources: [
        {
          name: "Crohn's & Colitis Foundation — Carolinas Chapter",
          type: 'Nonprofit chapter',
          website: 'https://www.crohnscolitisfoundation.org/chapters/carolinas',
          phone: '704-264-0587',
          email: 'carolinas@crohnscolitisfoundation.org',
          address: '8508 Park Road #157, Charlotte, NC 28210',
          notes: 'Local events, education, support groups, and volunteer opportunities across NC and SC.'
        },
        {
          name: "Crohn's & Colitis Foundation — Find NC Support Groups",
          type: 'Peer support',
          website: 'https://www.crohnscolitisfoundation.org/find-a-support-group',
          phone: '704-264-0587',
          notes: 'Filter by North Carolina on the support group finder for nearby or virtual meetings.'
        },
        {
          name: 'UNC Multidisciplinary Center for Inflammatory Bowel Disease',
          type: 'Academic IBD center (adult)',
          website: 'https://www.med.unc.edu/medicine/gi/patient-care/clinical-services/unc-center-for-inflammatory-bowel-disease/',
          phone: '984-974-5050',
          notes: 'Adult IBD care, infusion therapies, and multidisciplinary team at UNC Chapel Hill.'
        },
        {
          name: "UNC Children's Center for Pediatric IBD",
          type: 'Academic IBD center (pediatric)',
          website: 'https://www.med.unc.edu/medicine/gi/patient-care/clinical-services/unc-center-for-inflammatory-bowel-disease/',
          phone: '919-966-2435',
          notes: 'Pediatric Crohn’s disease and ulcerative colitis care.'
        },
        {
          name: 'Duke Health — Inflammatory Bowel Disease Clinic',
          type: 'Academic IBD center',
          website: 'https://medicine.duke.edu/divisions/gastroenterology/our-programs/inflammatory-bowel-disease',
          phone: '919-862-5015',
          notes: 'Crohn’s and colitis clinic; appointments via Duke Health (Option 1 for scheduling).'
        },
        {
          name: 'Wake Forest Baptist — IBD Program',
          type: 'Clinical IBD program',
          website: 'https://www.wakehealth.edu/specialty/Inflammatory-Bowel-Disease-IBD',
          phone: '336-716-2255',
          notes: 'IBD care in Winston-Salem; confirm current contact options on the hospital site.'
        }
      ]
    }
  },
  /** Default CCF chapter hint when a state has no custom entry yet */
  defaultChapterUrl: 'https://www.crohnscolitisfoundation.org/chapters',
  stateChapterHints: {
    AL: 'Tennessee/Alabama/NW Florida Chapter',
    AK: 'Northwest Chapter',
    AZ: 'Arizona Chapter',
    AR: 'North & Central Texas/Oklahoma Chapter',
    CA: 'Greater San Diego, Los Angeles, Northern California chapters',
    CO: 'Rocky Mountain Chapter',
    CT: 'Connecticut/Westchester Chapter',
    DE: 'Philadelphia/Delaware Valley Chapter',
    DC: 'DC/Maryland/Virginia Chapter',
    FL: 'Northeastern Florida / Tennessee-Alabama chapters (region varies)',
    GA: 'Georgia Chapter',
    HI: 'Northwest Chapter',
    ID: 'Northwest Chapter',
    IL: 'Illinois Chapter',
    IN: 'Indiana Chapter',
    IA: 'Nebraska/Iowa/South Dakota Chapter',
    KS: 'Heartland Chapter',
    KY: 'Kentucky/West Virginia Chapter',
    LA: 'Louisiana Chapter',
    ME: 'New England Chapter',
    MD: 'DC/Maryland/Virginia Chapter',
    MA: 'New England Chapter',
    MI: 'Michigan Chapter',
    MN: 'Minnesota/Dakotas Chapter',
    MS: 'Tennessee/Alabama/NW Florida Chapter',
    MO: 'Heartland Chapter',
    MT: 'Rocky Mountain Chapter',
    NE: 'Nebraska/Iowa/South Dakota Chapter',
    NV: 'Desert Mountain States Chapter',
    NH: 'New England Chapter',
    NJ: 'New Jersey Chapter',
    NM: 'Desert Mountain States Chapter',
    NY: 'Greater NYC, Upstate, Western NY chapters',
    NC: 'Carolinas Chapter',
    ND: 'Minnesota/Dakotas Chapter',
    OH: 'Northern Ohio Chapter',
    OK: 'North & Central Texas/Oklahoma Chapter',
    OR: 'Northwest Chapter',
    PA: 'Philadelphia/Delaware Valley or Western PA chapters',
    RI: 'New England Chapter',
    SC: 'Carolinas Chapter',
    SD: 'Nebraska/Iowa/South Dakota Chapter',
    TN: 'Tennessee/Alabama/NW Florida Chapter',
    TX: 'North & Central Texas or Southern Texas chapters',
    UT: 'Desert Mountain States Chapter',
    VT: 'New England Chapter',
    VA: 'DC/Maryland/Virginia Chapter',
    WA: 'Northwest Chapter',
    WV: 'Kentucky/West Virginia Chapter',
    WI: 'Wisconsin Chapter',
    WY: 'Rocky Mountain Chapter'
  }
};
