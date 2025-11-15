<script lang="ts">
	let selectedYear = '';
	let selectedCC = '';
	let selectedUni = '';
    let selectedMajor = '';

	let fileInput: HTMLInputElement;
	let selectedFileName = '';

	const academicYears = [
        '2025-2026', '2024-2025', '2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020',
        '2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015', '2013-2014', '2012-2013',
        '2011-2012', '2010-2011', '2009-2010', '2008-2009', '2007-2008', '2006-2007', '2005-2006',
        '2004-2005', '2003-2004', '2002-2003', '2001-2002', '2000-2001', '1999-2000', '1998-1999',
        '1997-1998', '1996-1997', '1995-1996', '1994-1995', '1993-1994', '1992-1993', '1991-1992',
        '1990-1991', '1989-1990', '1988-1989', '1987-1988', '1986-1987', '1985-1986'
    ];
	const communityColleges = [
		"Allan Hancock College",
        "American River College",
        "Antelope Valley College",
        "Bakersfield College",
        "Barstow Community College",
        "Berkeley City College",
        "Butte College",
        "Cabrillo College",
        "Calbright College",
        "Cañada College",
        "Cerritos College",
        "Cerro Coso Community College",
        "Chabot College",
        "Chaffey College",
        "Citrus College",
        "City College of San Francisco",
        "Clovis Community College",
        "Coastline College",
        "College of Alameda",
        "College of Marin",
        "College of San Mateo",
        "College of the Canyons",
        "College of the Desert",
        "College of the Redwoods",
        "College of the Sequoias",
        "College of the Siskiyous",
        "Columbia College",
        "Compton College",
        "Contra Costa College",
        "Copper Mountain College",
        "Cosumnes River College",
        "Crafton Hills College",
        "Cuesta College",
        "Cuyamaca College",
        "Cypress College",
        "DeAnza College",
        "Diablo Valley College",
        "East Los Angeles College",
        "El Camino College",
        "Evergreen Valley College",
        "Feather River College",
        "Folsom Lake College",
        "Foothill College",
        "Fresno City College",
        "Fullerton College",
        "Gavilan College",
        "Glendale Community College",
        "Golden West College",
        "Grossmont College",
        "Hartnell College",
        "Imperial Valley College",
        "Irvine Valley College",
        "Lake Tahoe Community College",
        "Laney College",
        "Las Positas College",
        "Lassen College",
        "Long Beach City College",
        "Los Angeles City College",
        "Los Angeles Harbor College",
        "Los Angeles Mission College",
        "Los Angeles Pierce College",
        "Los Angeles Southwest College",
        "Los Angeles Trade-Tech College",
        "Los Angeles Valley College",
        "Los Medanos College",
        "Madera Community College",
        "Mendocino College",
        "Merced College",
        "Merritt College",
        "MiraCosta College",
        "Mission College",
        "Modesto Junior College",
        "Monterey Peninsula College",
        "Moorpark College",
        "Moreno Valley College",
        "Mt. San Antonio College",
        "Mt. San Jacinto College",
        "Napa Valley College",
        "Norco College",
        "North Orange Continuing Education",
        "Ohlone College",
        "Orange Coast College",
        "Oxnard College",
        "Palo Verde College",
        "Palomar College",
        "Pasadena City College",
        "Porterville College",
        "Reedley College",
        "Rio Hondo College",
        "Riverside City College",
        "Sacramento City College",
        "Saddleback College",
        "San Bernardino Valley College",
        "San Diego City College",
        "San Diego College of Continuing Education",
        "San Diego Mesa College",
        "San Diego Miramar College",
        "San Joaquin Delta College",
        "San Jose City College",
        "Santa Ana College",
        "Santa Barbara City College",
        "Santa Monica College",
        "Santa Rosa Junior College",
        "Santiago Canyon College",
        "Shasta College",
        "Sierra College",
        "Skyline College",
        "Solano Community College",
        "Southwestern College",
        "Taft College",
        "Ventura College",
        "Victor Valley College",
        "Coalinga College",
        "Lemoore College",
        "West Los Angeles College",
        "West Valley College",
        "Woodland Community College",
        "Yuba College"
	];
	const universities = [
		"California Maritime Academy",
        "California Polytechnic University, Humboldt",
        "California Polytechnic University, Pomona",
        "California Polytechnic University, San Luis Obispo",
        "California State University, Bakersfield",
        "California State University, Channel Islands",
        "California State University, Chico",
        "California State University, Dominguez Hills",
        "California State University, East Bay",
        "California State University, Fresno",
        "California State University, Fullerton",
        "California State University, Hayward",
        "California State University, Long Beach",
        "California State University, Los Angeles",
        "California State University, Maritime Academy",
        "California State University, Monterey Bay",
        "California State University, Northridge",
        "California State University, Sacramento",
        "California State University, San Bernardino",
        "California State University, San Marcos",
        "California State University, Stanislaus",
        "Humboldt State University",
        "San Diego State University",
        "San Francisco State University",
        "San Jose State University",
        "Sonoma State University",
        "University of California, Berkeley",
        "University of California, Davis",
        "University of California, Irvine",
        "University of California, Los Angeles",
        "University of California, Merced",
        "University of California, Riverside",
        "University of California, San Diego",
        "University of California, Santa Barbara",
        "University of California, Santa Cruz",
        "Azusa Pacific University",
        "California Lutheran University",
        "Fresno Pacific University",
        "Loyola Marymount University",
        "National University",
        "Palo Alto University",
        "Pepperdine University",
        "Simpson University",
        "University of Redlands",
        "University of the Pacific"
	];
    const majors = [
		"Accounting",
        "Acting",
        "African American Studies",
        "African Studies",
        "Agribusiness",
        "Agricultural Engineering",
        "Agriculture",
        "Anatomy & Physiology",
        "Animal Science",
        "Anthropology",
        "Applied Mathematics",
        "Arabic",
        "Archeology",
        "Architecture",
        "Art History",
        "Art Therapy",
        "Artificial Intelligence",
        "Asian Studies",
        "Astronomy",
        "Atmospheric Science",
        "Automotive Technology",
        "Aviation Science",
        "Biochemistry",
        "Biology",
        "Biomedical Engineering",
        "Biomedical Science",
        "Broadcast Journalism",
        "Business Administration",
        "Business Analytics",
        "Chemical Engineering",
        "Chemistry",
        "Chinese",
        "Civil Engineering",
        "Classics",
        "Cloud Computing",
        "Cognitive Science",
        "Communications",
        "Comparative Literature",
        "Computer Engineering",
        "Computer Science",
        "Construction Management",
        "Creative Writing",
        "Criminal Justice",
        "Criminology",
        "Curriculum & Instruction",
        "Cybersecurity",
        "Dance",
        "Data Analytics",
        "Data Science",
        "Dental Hygiene",
        "Digital Humanities",
        "Digital Media",
        "Early Childhood Education",
        "Earth Science",
        "Economics",
        "Educational Leadership",
        "Electrical Engineering",
        "Elementary Education",
        "Emergency Management",
        "English",
        "Entrepreneurship",
        "Environmental Engineering",
        "Environmental Science",
        "Environmental Studies",
        "Exercise Science",
        "Fashion Design",
        "Film & Television Production",
        "Film Production",
        "Film Studies",
        "Finance",
        "Fire Science",
        "Fisheries & Wildlife",
        "Food Science",
        "Forestry",
        "French",
        "Game Design",
        "Game Development",
        "Gender Studies",
        "Genetics",
        "Geography",
        "Geology",
        "German",
        "Global Studies",
        "Graphic Design",
        "Health Sciences",
        "History",
        "Horticulture",
        "Homeland Security",
        "Hospitality Management",
        "Human Resource Management",
        "Human–Computer Interaction",
        "Indigenous Studies",
        "Industrial Engineering",
        "Information Systems",
        "Information Technology",
        "Interior Design",
        "Interdisciplinary Studies",
        "International Business",
        "International Relations",
        "Italian",
        "Japanese",
        "Journalism",
        "Kinesiology",
        "Korean",
        "Latin American Studies",
        "Legal Studies",
        "Liberal Studies",
        "Linguistics",
        "Management",
        "Marine Biology",
        "Marketing",
        "Materials Science Engineering",
        "Mathematics",
        "Mechanical Engineering",
        "Mechatronics Engineering",
        "Media Studies",
        "Middle Eastern Studies",
        "Microbiology",
        "Molecular Biology",
        "Music",
        "Music Education",
        "Music Performance",
        "Music Theory",
        "Network Engineering",
        "Neuroscience",
        "Nuclear Engineering",
        "Nursing",
        "Nutrition & Dietetics",
        "Occupational Therapy",
        "Petroleum Engineering",
        "Philosophy",
        "Photography",
        "Physical Education",
        "Physical Therapy",
        "Physics",
        "Political Science",
        "Pre-Dental",
        "Pre-Law",
        "Pre-Med",
        "Pre-Pharmacy",
        "Psychology",
        "Public Administration",
        "Public Health",
        "Public Policy",
        "Public Relations",
        "Radiologic Technology",
        "Real Estate",
        "Religious Studies",
        "Respiratory Therapy",
        "Retail Management",
        "Robotics",
        "Russian",
        "Secondary Education",
        "Social Work",
        "Sociology",
        "Software Engineering",
        "Spanish",
        "Special Education",
        "Sports Communication",
        "Statistics",
        "Studio Art",
        "Structural Engineering",
        "Supply Chain Management",
        "Sustainability Studies",
        "Theater Arts",
        "Urban Studies",
        "Welding Technology",
        "Wildlife Biology"
	];

	function triggerFileClick() {
		fileInput.click();
	}

	function handleFileChange(e: Event) {
		const target = e.target as HTMLInputElement;
		if (target.files && target.files.length > 0) {
			selectedFileName = target.files[0].name;
			console.log('File selected:', selectedFileName);
		} else {
			selectedFileName = '';
		}
	}
</script>

<div class="form-container">
	<h3>Transfer Information</h3>

	<div class="form-group">
		<label for="academic-year">Academic Year</label>
		<select id="academic-year" bind:value={selectedYear}>
			<option disabled value="">Select Year...</option>
			{#each academicYears as year}
				<option value={year}>{year}</option>
			{/each}
		</select>
	</div>

    <div class="form-group">
		<label for="major">Major</label>
		<select id="major" bind:value={selectedMajor}>
			<option disabled value="">Select Major...</option>
			{#each majors as major}
				<option value={major}>{major}</option>
			{/each}
		</select>
	</div>

	<div class="form-group">
		<label for="community-college">Institution</label>
		<select id="community-college" bind:value={selectedCC}>
			<option disabled value="">Select CC...</option>
			{#each communityColleges as cc}
				<option value={cc}>{cc}</option>
			{/each}
		</select>
	</div>

	<div class="form-group">
		<label for="university">Agreements with Other Institutions</label>
		<select id="university" bind:value={selectedUni}>
			<option disabled value="">Select University...</option>
			{#each universities as uni}
				<option value={uni}>{uni}</option>
			{/each}
		</select>
	</div>

	<div class="form-group">
		<label for="file-attach">Attach File</label>
		<input
			type="file"
			id="file-attach"
			bind:this={fileInput}
			on:change={handleFileChange}
			hidden
		/>
		<button type="button" class="attach-button" on:click={triggerFileClick}>
			📎 Attach File
		</button>
		
		{#if selectedFileName}
			<span class="file-name">{selectedFileName}</span>
		{/if}
	</div>
</div>

<style>
	.form-container {
		border: 2px solid black;
		border-radius: 16px;
		padding: 16px;
		background-color: #9370DB;
		font-family: sans-serif;
	}

	h3 {
		text-align: center;
		margin-top: 0;
		color: white;
        margin-bottom: 15px;
	}

	.form-group {
		margin-bottom: 16px;
	}

	.form-group label {
		display: block;
		margin-bottom: 6px;
		font-weight: bold;
		color: white;
	}

	select {
		width: 100%;
		padding: 10px;
		border-radius: 8px;
		border: 1px solid #ccc;
		background-color: white;
		font-size: 1em;
		box-sizing: border-box;
		cursor: pointer;
        color: black;
	}

	.attach-button {
		padding: 10px 15px;
		border: 1px solid #6A5ACD; 
		background-color: #6A5ACD;
		color: white;
		border-radius: 8px;
		cursor: pointer;
		font-size: 1em;
		font-weight: bold;
	}

	.file-name {
		display: inline-block;
		margin-left: 12px;
		font-style: italic;
		color: #333;
	}
</style>