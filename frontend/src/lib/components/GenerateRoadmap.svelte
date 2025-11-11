<script lang="ts">
	import { tick } from 'svelte';
	let currentMessage = '';
	let chatLogContainer: HTMLDivElement | null = null;

	let chatLogs: { sender: 'user' | 'ai'; text: string }[] = [
		{ sender: 'ai', text: 'Roadmap shows up here eventually' } 
	];

	function handleSubmit() {
		if (!currentMessage.trim()) return; 

		console.log('User message:', currentMessage);

		chatLogs = [...chatLogs, { sender: 'user', text: currentMessage }];

		currentMessage = '';

		tick().then(() => {
			if (chatLogContainer) {
			chatLogContainer.scrollTo({
				top: chatLogContainer.scrollHeight,
				behavior: 'smooth'
			});
			}
		});
	}
</script>

<div class="roadmap-generator">
	<h3>Generate a Roadmap</h3>

	<div class="chat-log" bind:this={chatLogContainer}>
		{#each chatLogs as log}
			<div class="chat-bubble {log.sender}">
				{log.text}
			</div>
		{/each}
	</div>

	<form class="chat-input" on:submit|preventDefault={handleSubmit}>
		<input
			type="text"
			bind:value={currentMessage}
			placeholder="Text..."
		/>
		<button type="submit">↑</button>
	</form>
</div>

<style>
	.roadmap-generator {
		display: flex;
		flex-direction: column;
		min-height: 0;
		max-height: 70vh;
		border: 2px solid black;
		border-radius: 16px;
		padding: 12px;
		box-sizing: border-box;
        background-color: rgb(120, 60, 120);
		overflow: hidden;
	}

	h3 {
		text-align: center;
		margin-top: 0;
		font-weight: normal;
        padding-bottom: 15px;
        color: white;
	}

	.chat-log {
		flex-grow: 1;
		overflow-y: auto;
		min-height: 0;
		border: 2px solid black;
		border-radius: 12px;
		padding: 12px;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.chat-bubble {
		padding: 8px 12px;
		border-radius: 10px;
		max-width: 85%;
		word-wrap: break-word;
        color: white;
	}

	.chat-bubble.ai {
        background-color: rgb(117, 23, 117);
		align-self: flex-start;
	}

	.chat-bubble.user {
		background-color: rgb(214, 8, 214);
		align-self: flex-end;
	}

	.chat-input {
		display: flex;
		margin-top: 12px;
        color: black;
	}

	.chat-input input {
		flex-grow: 1;
		border: 1px solid black;
		border-radius: 16px;
		padding: 8px 12px;
		margin-right: 8px;
		background-color: rgb(214, 8, 214);
		color: white;
	}

	.chat-input button {
		padding: 0 12px;
		border: 1px solid black;
		background-color: rgb(214, 8, 214);
		color: white;
		border-radius: 50%;
		cursor: pointer;
		font-size: 1.2em;
		font-weight: bold;
	}

	input::placeholder {
        color: white; 
    }
</style>