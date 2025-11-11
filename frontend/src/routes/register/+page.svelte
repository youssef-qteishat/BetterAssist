<script lang="ts">
	import { Jumper } from 'svelte-loading-spinners';
	import { fade } from 'svelte/transition';

	let firstName: string = '';
	let lastName: string = '';
	let email: string = '';
	let password: string = '';
	let confirmPassword: string = '';
	let loading: boolean = false;
	let success: boolean = false;
	let error: string = '';
	let visible: boolean = false;
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

	async function handleRegister(e: Event) {
		e.preventDefault();
		loading = true;
		error = '';
		success = false;
		visible = false;
		clearTimeout(messageTimeout);

		if (password !== confirmPassword) {
			error = 'Passwords do not match!';
			loading = false;
			showMessage();
			return;
		}

		try {
			console.log('Registering user with:', { firstName, lastName, email, password });
			const response: Response = await fetch('http://localhost:8000/api/auth/register', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ firstName, lastName, email, password })
			});

			if (response.ok) {
				console.log('Registration successful!');
				console.log('Response:', response);
				success = true;
				showMessage();
				// window.location.href = '/login';
			} else {
				const errorData = await response.json();
				console.error('Registration failed:', errorData);
				error = errorData.detail || 'Unknown error';
				showMessage();
			}
		} catch (error: any) {
			console.error('Error during registration:', error);
			error = error.message || 'An error occurred. Please try again later.';
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
			Sign up for an account
		</h2>
	</div>

	<div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
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
				<p class="text-green-500 p-2">
					Registration success! Please check your email to confirm your account.
				</p>
			</div>
		{/if}
		<form action="#" method="POST" class="space-y-6">
			<div>
				<label for="firstName" class="block text-sm/6 font-medium text-gray-100">First Name</label>
				<div class="mt-2">
					<input
						id="firstName"
						type="text"
						name="firstName"
						required
						autocomplete="given-name"
						class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
						bind:value={firstName}
					/>
				</div>
			</div>
			<div>
				<label for="lastName" class="block text-sm/6 font-medium text-gray-100">Last Name</label>
				<div class="mt-2">
					<input
						id="lastName"
						type="text"
						name="lastName"
						required
						autocomplete="family-name"
						class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
						bind:value={lastName}
					/>
				</div>
			</div>
			<div>
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
				<label for="password" class="block text-sm/6 font-medium text-gray-100">Password</label>
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
				<label for="confirm-password" class="block text-sm/6 font-medium text-gray-100"
					>Confirm Password</label
				>
				<div class="mt-2">
					<input
						id="confirm-password"
						type="password"
						name="confirm-password"
						required
						class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
						bind:value={confirmPassword}
					/>
				</div>
			</div>

			<div>
				{#if loading}
					<Jumper size="25" color="#ffffff" unit="px" duration="1s" />
				{:else}
					<button
						type="submit"
						class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm/6 font-semibold text-white hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
						on:click={handleRegister}>Sign Up</button
					>
				{/if}
			</div>

			<div class="flex justify-center">
				<a href="/" class="font-semibold text-indigo-400 hover:text-indigo-300"
					>Already have an account?</a
				>
			</div>
		</form>
	</div>
</div>
