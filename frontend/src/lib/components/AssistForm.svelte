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
		'De Anza College',
		'Foothill College',
		'Mission College',
		'Evergreen Valley College'
	];
	const universities = [
		'San Jose State University',
		'UC Berkeley',
		'Stanford University',
		'Santa Clara University'
	];
    const majors = [
		'Computer Science',
		'Engineering',
		'Business Administration',
		'Psychology',
		'Biology',
		'Art',
		'English'
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