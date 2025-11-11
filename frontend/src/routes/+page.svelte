<script lang="ts">
	import { goto } from '$app/navigation';
	import { sessionStore } from '$lib/sessionStore';
	import { Jumper } from 'svelte-loading-spinners';
	import { fade } from 'svelte/transition';
	let email = '';
	let password = '';
	let loading = false;
	let success = false;
	let error = '';
	let visible = false;
	let messageTimeout: NodeJS.Timeout;

	function showMessage() {
		clearTimeout(messageTimeout);
		visible = true;
		messageTimeout = setTimeout(() => {
			visible = false;
			error = '';
			success = false;
		}, 3000);
	}

	async function handleSubmit(e: Event) {
		e.preventDefault();
		loading = true;
		error = '';
		success = false;
		visible = false;
		clearTimeout(messageTimeout);

		try {
			const response = await fetch('http://localhost:8000/api/auth/login', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email, password })
			});

			const data = await response.json();
			console.log('data', data);
			if (!response.ok) {
				error = data.detail || 'Login failed';
				showMessage();
				return;
			}

			if (data.user?.id) {
				success = true;
				sessionStore.set({ user: data.user, session: data.session });
				showMessage();
				// Don't reset success state before navigation
				setTimeout(() => goto(`/user/${data.user.id}`), 2000);
			}
		} catch (err: any) {
			error = err.message;
			showMessage();
		} finally {
			loading = false;
		}
	}
</script>

<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
	<h1 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-white">
		BetterAssist: Transfer Planning Simplified
	</h1>
	<div class="sm:mx-auto sm:w-full sm:max-w-sm">
		<img src="./../better-assist-logo.png" alt="Your Company" class="mx-auto h-24 w-auto mt-10" />
		<h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-white">
			Sign in to your account
		</h2>
	</div>

	<div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
		<form action="#" method="POST" class="space-y-6">
			<div>
				{#if error && visible}
					<div
						transition:fade={{ duration: 200 }}
						class="flex items-center justify-center bg-red-500/10 border-2 border-red-500 rounded-md mb-2"
						on:outroend={() => {
							error = '';
							success = false;
						}}
					>
						<p class="text-red-500 p-2">{error}</p>
					</div>
				{:else if success && visible}
					<div
						transition:fade={{ duration: 200 }}
						class="flex items-center justify-center bg-green-500/10 border-2 border-green-500 rounded-md mb-2"
						on:outroend={() => {
							error = '';
							success = false;
						}}
					>
						<p class="text-green-500 p-2">Login success! Loading user page...</p>
					</div>
				{/if}
				<label for="email" class="block text-sm/6 font-medium text-gray-100">Email address</label>
				<div class="mt-2">
					<input
						id="email"
						type="email"
						name="email"
						required
						autocomplete="email"
						class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
						bind:value={email}
					/>
				</div>
			</div>

			<div>
				<div class="flex items-center justify-between">
					<label for="password" class="block text-sm/6 font-medium text-gray-100">Password</label>
				</div>
				<div class="mt-2">
					<input
						id="password"
						type="password"
						name="password"
						required
						autocomplete="current-password"
						class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
						bind:value={password}
					/>
				</div>
			</div>

			<div>
				<button
					type="submit"
					class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm/6 font-semibold text-white hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
					on:click={handleSubmit}
				>
					{#if loading}
						<Jumper size="25" color="#ffffff" unit="px" duration="1s" />
					{:else}
						Sign in
					{/if}
				</button>
			</div>

			<div class="flex justify-center">
				<a href="/register" class="font-semibold text-indigo-400 hover:text-indigo-300"
					>Don't have an account?</a
				>
			</div>
		</form>
	</div>
</div>
