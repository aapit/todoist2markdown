# Markdown note extractor for Todoist 
Keep your Todoist clean from stuff that doesn't require your action.

## What it does
This Python script looks for tasks in Todoist tagged with '`note`'.
It then writes the task content to a Markdown file, using a template.
Next, the task is completed in Todoist.

## Why?
It enables you to jolt down some quick scribbles, using Todoist's easy interface.
The danger of doing this is that your todo list is polluted with notes.
And these notes don't directly translate into actions.
That's why they shouldn't distract you from what you were planning to do.

## QuickStart
Just tag the task in Todoist's Quick Add with `note`.
For instance by using `@note` in the task text.
This script then turns this type of task into a Markdown file on disk.
From then on, you can search for it when you need a reference.
But no longer being on your radar, you can spend your focus on your actual goals.

You could trigger it from a cronjob to periodically do maintenance on your todos.

## Credits
By David Spreekmeester | [@aapit](https://github.com/aapit)

This unofficial script is not condoned in any way by Doist.
Please do not sue me if any dogs explode in microwaves 🐶💥
