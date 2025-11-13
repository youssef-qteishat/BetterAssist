<script lang="ts">
	// Array of placeholder roadmap items
	const roadmaps = [
		{ id: 1, title: 'Computer Science - UC Berkeley', description: '3-year plan' },
		{ id: 2, title: 'Biomedical Engineering - UCSD', description: '2-year plan' },
		{ id: 3, title: 'Medicine - UCSF', description: '2-year plan' },
		{ id: 4, title: 'Cybersecurity - UCLA', description: '1-year plan' },
		{ id: 5, title: 'AI & Machine Learning - Stanford', description: '1-year plan' }
	];

	function selectRoadmap(roadmapId: number) {
		// Handle roadmap selection
		console.log('Selected roadmap:', roadmapId);
	}
</script>

<div class="roadmap-container">
	<div class="roadmap-header">
		<h3>My Roadmaps</h3>
		<p class="subtitle">Select a roadmap to view or edit</p>
	</div>

	<div class="roadmap-list">
		{#each roadmaps as roadmap}
			<div class="roadmap-item">
				<div class="roadmap-emoji">📚</div>
				<div class="roadmap-details">
					<h4>{roadmap.title}</h4>
					<p>{roadmap.description}</p>
				</div>
				<div class="roadmap-arrow">→</div>
				<button on:click={() => selectRoadmap(roadmap.id)}>View</button>
			</div>
		{/each}

		<!-- Add New Roadmap Button -->
		<button class="add-roadmap-btn">
			<span>+</span> Create New Roadmap
		</button>
	</div>
</div>

<style>
	.roadmap-container {
		background: white;
		border-radius: 12px;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		padding: 1.5rem;
		width: 100%;
		max-width: 600px;
		margin: 2rem auto;
	}

	.roadmap-header {
		margin-bottom: 1.5rem;
		text-align: center;
	}

	.roadmap-header h3 {
		margin: 0 0 0.5rem 0;
		font-size: 1.5rem;
		color: #2d3748;
	}

	.subtitle {
		margin: 0;
		color: #718096;
		font-size: 0.9rem;
	}

	.roadmap-list {
		max-height: 400px;
		overflow-y: auto;
		padding-right: 0.5rem;
	}

	.roadmap-item {
		display: flex;
		align-items: center;
		padding: 1rem;
		margin-bottom: 0.75rem;
		background: #f7fafc;
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.2s ease;
		border: 1px solid #e2e8f0;
	}

	.roadmap-item:hover {
		transform: translateY(-2px);
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		border-color: #cbd5e0;
	}

	.roadmap-emoji {
		font-size: 1.5rem;
		margin-right: 1rem;
		flex-shrink: 0;
	}

	.roadmap-details {
		flex-grow: 1;
	}

	.roadmap-details h4 {
		margin: 0 0 0.25rem 0;
		color: #2d3748;
		font-size: 1rem;
	}

	.roadmap-details p {
		margin: 0;
		color: #718096;
		font-size: 0.85rem;
	}

	.roadmap-arrow {
		color: #a0aec0;
		font-size: 1.25rem;
		margin-left: 0.5rem;
	}

	.add-roadmap-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		padding: 0.75rem;
		margin-top: 0.5rem;
		background: #f7fafc;
		border: 2px dashed #cbd5e0;
		border-radius: 8px;
		color: #4a5568;
		font-size: 0.9rem;
		cursor: pointer;
		transition: all 0.2s ease;
	}

	.add-roadmap-btn:hover {
		background: #edf2f7;
		border-color: #a0aec0;
	}

	.add-roadmap-btn span {
		font-size: 1.25rem;
		margin-right: 0.5rem;
	}

	/* Custom scrollbar */
	.roadmap-list::-webkit-scrollbar {
		width: 6px;
	}

	.roadmap-list::-webkit-scrollbar-track {
		background: #f1f1f1;
		border-radius: 10px;
	}

	.roadmap-list::-webkit-scrollbar-thumb {
		background: #cbd5e0;
		border-radius: 10px;
	}

	.roadmap-list::-webkit-scrollbar-thumb:hover {
		background: #a0aec0;
	}
</style>
