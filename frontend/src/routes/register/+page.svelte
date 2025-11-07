<script lang="ts">
    let email = '';
    let password = '';
    let confirmPassword = ''; // New variable for confirm password

    async function handleRegister(e: Event) {
        e.preventDefault();

        // Check if passwords match
        if (password !== confirmPassword) {
            console.error('Passwords do not match!');
            return;
        }

        const response = await fetch('http://localhost:8000/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        console.log(response);
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
        <form action="#" method="POST" class="space-y-6">
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
                <label for="confirm-password" class="block text-sm/6 font-medium text-gray-100">Confirm Password</label>
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
                <button
                    type="submit"
                    class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm/6 font-semibold text-white hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
                    on:click={handleRegister}>Sign Up</button
                >
            </div>

            <div class="flex justify-center">
                <a href="/" class="font-semibold text-indigo-400 hover:text-indigo-300">Already have an account?</a>
            </div>
        </form>
    </div>
</div>