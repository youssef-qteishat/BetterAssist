<script lang="ts">
	let currentMessage = '';

	let chatLogs: { sender: 'user' | 'ai'; text: string }[] = [
		{ sender: 'ai', text: 'Roadmap shows up here eventually' } 
	];

	function handleSubmit() {
		if (!currentMessage.trim()) return; 

		console.log('User message:', currentMessage);

		chatLogs = [...chatLogs, { sender: 'user', text: currentMessage }];

		currentMessage = '';
	}
</script>

<div class="roadmap-generator">
	<h3>Generate a Roadmap</h3>

	<div class="chat-log">
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
		height: 100%;
		border: 2px solid black;
		border-radius: 16px;
		padding: 12px;
		box-sizing: border-box;
        background-color: white;
	}

	h3 {
		text-align: center;
		margin-top: 0;
		font-weight: normal;
        padding-bottom: 15px;
        color: black;
	}

	.chat-log {
		flex-grow: 1;
		border: 2px solid black;
		border-radius: 12px;
		padding: 12px;
		overflow-y: auto;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.chat-bubble {
		padding: 8px 12px;
		border-radius: 10px;
		max-width: 85%;
		word-wrap: break-word;
        color: black;
	}

	.chat-bubble.ai {
        background-color: gray;
		align-self: flex-start;
	}

	.chat-bubble.user {
		background-color: lightblue;
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
	}

	.chat-input button {
		padding: 0 12px;
		border: 1px solid black;
		background-color: white;
		color: black;
		border-radius: 50%;
		cursor: pointer;
		font-size: 1.2em;
		font-weight: bold;
	}
</style>