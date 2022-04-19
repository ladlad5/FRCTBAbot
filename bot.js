const { SlashCommandBuilder } = require('@discordjs/builders');
const {Client, Intents} = require('discord.js');
const {token} = require('./config.json');
const client = new Client({ intents: [Intents.FLAGS.GUILDS]});
client.login(token);

const commands = [
    new SlashCommandBuilder().setName("ping").setDescription("hi sisters")
]