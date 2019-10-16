# Markdown note extractor for Todoist 
Keep your Todoist clean from stuff that doesn't require your action.

## What it does
This Python script looks for tasks in Todoist tagged with triggers specified by you.
For instance you could use the tag `note`, `recipe`, `movie`, `music`, `idea` or `present`.

It then writes the task content to a Markdown file, using a template. 
Next to the task text it also includes the comments on the task, the labels and its creation date.

Next, the task is completed in Todoist.

## Why?
It enables you to jolt down some quick scribbles, using Todoist's easy interface.
The danger of doing this is that your todo list is polluted with notes.
And these notes don't directly translate into actions.

That's why they shouldn't distract you from what you were planning to do.

You can let this script keep your Todoist spiffy clean on a regular basis.

## QuickStart
1. Configure environment
Create a `.env` file and fill it with your config values. You can use `.env.template` as an example.

2. Set your routines
Use `routines.template.yaml` as an example to create your own `routines.yaml`.
Configuring `appendFilename` adds a tagged todo item to a bundled note where all items with this tag are stored. Not setting this parameter creates a new note for every task.

3. Tag your todos
Just tag your new task in Todoist with `note`.
For instance by typing `@note` in Quick Add's task text.
This script then turns this type of task into a Markdown file on disk.
From then on, you can search for it when you need a reference.
But no longer being on your radar, you can spend your focus on your actual goals.

You could trigger it from a cronjob to periodically do maintenance on your todos.

## Credits
By David Spreekmeester | [@aapit](https://github.com/aapit)

This unofficial script is not condoned in any way by Doist.
Please do not sue me if any dogs explode in microwaves 🐶💥
