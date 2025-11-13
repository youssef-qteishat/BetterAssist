<script lang="ts">
	import { sessionStore } from '$lib/sessionStore';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import GenerateRoadmap from '$lib/components/GenerateRoadmap.svelte';
	import RoadmapBox from '$lib/components/RoadmapBox.svelte';

	$: user = $sessionStore?.user;
	$: meta = $sessionStore?.user?.user_metadata;

	onMount(() => {
		if (!$sessionStore) {
			console.log('No session found, redirecting to login.');
			goto('/');
		}
	});

	async function handleLogout() {
		sessionStore.set(null);
		await goto('/');
	}
</script>

{#if user && meta}
	<h1 class="welcome-text">Hi {meta.first_name}!</h1>
	<button on:click={handleLogout} class="logout-button-top-right">Log Out</button>
	<div>
		<RoadmapBox />
		<GenerateRoadmap />
	</div>
{:else}
	<p>Loading user data...</p>
{/if}

<style>
	:global(body) {
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 100vh;
		background-color: gray;
		margin: 0;
	}

	.welcome-text {
		position: absolute;
		top: 40px;
		left: 50%;
		transform: translateX(-50%);
		font-size: 1.5em;
		font-weight: normal;
		z-index: 10;
		margin: 0;
		padding: 0;
	}

	.logout-button-top-right {
		position: absolute;
		top: 25px;
		right: 25px;
		background-color: red;
		border: 1px solid black;
		border-radius: 8px;
		padding: 8px 12px;
		cursor: pointer;
		font-size: 0.9em;
		z-index: 10;
	}
</style>

<style>
	:global(body) {
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 100vh;
		background-color: gray;
		margin: 0;
	}

	.welcome-text {
		position: absolute;
		top: 40px;
		left: 50%;
		transform: translateX(-50%);
		font-size: 1.5em;
		font-weight: normal;
		z-index: 10;
		margin: 0;
		padding: 0;
	}

	.logout-button-top-right {
		position: absolute;
		top: 25px;
		right: 25px;
		background-color: red;
		border: 1px solid black;
		border-radius: 8px;
		padding: 8px 12px;
		cursor: pointer;
		font-size: 0.9em;
		z-index: 10;
	}
</style>