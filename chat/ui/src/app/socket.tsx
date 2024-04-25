"use client";

import { io } from "socket.io-client";

export const socket = io(`ws://${document.location.hostname}:3001`);