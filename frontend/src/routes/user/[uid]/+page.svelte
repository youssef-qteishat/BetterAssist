<script lang="ts">
	import { sessionStore } from '$lib/sessionStore';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

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
	<h1>Welcome, {meta.first_name} {meta.last_name}!</h1>

	<p>Your email is: {user.email}</p>
	<p>Your UID is: {user.id}</p>

	<button on:click={handleLogout}> Log Out </button>
{:else}
	<p>Loading user data...</p>
{/if}