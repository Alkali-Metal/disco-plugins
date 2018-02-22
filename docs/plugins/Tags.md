# Tags


## Overview

This plugin allows you to create custom commands within each server independantly as well as globally (global are only able to be created by users which have at least the global admin rank)

</br>

-------------------------------------------

</br>

## Commands

<a id="options-list"></a>

### Forewarning:
When running most of the commands within this plugin, we have a slightly weird command syntax for it. Instead of using positional arguments for the variables, we use what we are deeming "options", what this entails is that they can be in any order within the command itself and only certain options are mandatory for each command as most of them have defaults that will be set if the option is not given by the user.
|  Option  | Type     | Description | Default |
| -------- | -------- | ----------- | ------- |
| name     | String   | The name of the tag, this is how users will call the tag from a message. |  |
| response | String   | This is what the bot will respond to with the tag. (This is the main body of the embed if `embed` set to `true`) |  |
| embed    | Bool     | Tells the bot whether to embed this response or not. | False |
| content  | String   | What the actual content of the message with the embed will have. | Tag embed: |
| title    | String   | What the title of the embed will have as its content. |  |
| url      | String   | The hyperlinked URL that the title will point to. | (This documentation) |
| colour   | Hex code | The colour of the side bar of the embed. | 7289DA |
| footer   | String   | The content within the footer. |  |
| level    | Integer  | The permission level required to run the command. | 0 |
| global   | Bool     | Whether or not the tag will be made as a global tag or not. Only global administrators can set this to true. | False |

</br>
</br>

### Add

This command allows you to add a tag. Aliased to `create`.

> **Syntax:** `{Command Prefix}tag add <Options...>`
>
> [See](#options-list) for the list of valid options and what they do.

Examples:
```
[Alkali] !tag add --response=Well hello there --name=Ohai there
[Bot] Tag created with name "ohai-there"
---------------------------------
[Alkali] !tag create --name=spam --title=ingredients --response=eggs --content= --embed=1 --global=false --footer=recipe for POTATO SALAD
[Bot] Tag created with name "spam"
---------------------------------
[Alkali] !tag add --response=salad --embed=false
[Bot] Missing argument. ("name")
```

</br>

-------------------------------------------

</br>

## Example Configuration

This configuration is in the guild's configuration file under `tags`. But the bot will set it up correctly if the user runs the `tag setup` command.

```json
{
  "list": {},
  "options": {
    "log_channel": null,
    "allow_global": true,
    "logging": false
  }
}
```