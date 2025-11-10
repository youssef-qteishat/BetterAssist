import { writable } from 'svelte/store';
import { browser } from '$app/environment';

type SessionData = {
	user: any;
	session: any; 
} | null;

const initialValue: SessionData = browser
	? JSON.parse(window.localStorage.getItem('session') || 'null')
	: null;

export const sessionStore = writable<SessionData>(initialValue);

if (browser) {
	sessionStore.subscribe((value) => {
		if (value) {
			window.localStorage.setItem('session', JSON.stringify(value));
		} else {
			window.localStorage.removeItem('session');
		}
	});
}