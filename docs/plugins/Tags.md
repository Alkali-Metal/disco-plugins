# Tags


## Overview

This plugin allows you to create custom commands within each server independantly as well as globally (global are only able to be created by users which have at least the global admin rank)

</br>

-------------------------------------------

</br>

## Commands

### Add

This command allows you to add a tag.

> **Syntax:** `{Command Prefix}tag add <Options...>`
>
>This command is odd in the sense that it doesn't have any positional arguments but it has options. The only mandatory arguments are `name` and `response`. Valid options are as follows:</br>
> `name`: (Type: string) The name of the command, this is how people will call the command.</br>
> `response`: (Type: string) The response of the command, this is also what will be the main body text of the embed if you set `embed` to true.</br>
> `embed`: (Type: Boolean) Tells the bot whether or not you want the response as an embeded message. (Defaults to: `False`)</br>
> `colour`: (Type: hex code (excluding the `#`)) The hex colour for the side bar of the embed. (defaults to: `7289DA`)</br>
> `footer`: (Type: string) The footer text of the embed. (Defaults to: No text)</br>
> `level`: (Type: integer) The permission level of the command. Valid permission levels can be found [here]("Permission Levels") (Defaults to: `0`)</br>
> `content`: (Type: string) This is the text that appears before an embed. (Defaults to: `Tag embed:`)</br>
> `url`: (Type: string) This is the URL that the title of the embed points to. (Defaults to: Documentation URL)</br>
> `title`: (Type: string) This is the text of the title.(Defaults to: No text)</br>
> `global`: (Type: Boolean) This is what determines whether or not the tag will be created as a global tag or as a local only tag. (Defaults to: `False`)

Examples:
```
[1-3 examples]
```

</br>

-------------------------------------------

</br>

## Example Configuration

Configuration Name: `[Config File Name]`

```json
[Example Config]
```