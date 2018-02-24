# Tags

<a id="overview"></a>

## Overview

This plugin allows you to create custom commands within each server independantly as well as globally (global are only able to be created by users which have at least the global admin rank)

</br>

-------------------------------------------

</br>

<a id="commands"></a>

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
> See [here](#options-list) for the list of valid options and what they do.
> The mandatory options are `name` and `response` for this command.

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

### Remove

This command allows you to remove a tag. Aliased to `delete`.

> **Syntax:** `{Command Prefix}tag remove <name> [global]`
>
> `name`: The name of the tag you want to remove.  
> `global`: (Type: Bool) Indicates whether you are attempting to remove a global tag or not. Defaults to False

Examples:
```
[Alkali] !tag remove spam
[Bot] Removed tag with name `spam`. Data: <Data>
---------------------------------
[Alkali] !tag remove spam false
[Bot] Tag `spam` doesn't exist.
```

</br>

### Modify

This command allows you to modify an already existing tag. Aliased to `edit`

> **Syntax:** `{Command Prefix}tag modify <Options...>`
>
> See [here](#options-list) for a list of options and their valid data types.
> The only mandatory option is `name` and it will overwrite the existing data for any other option given.

Examples:
```
[Alkali] !tag modify --name=spam --response=eggs --content=foo --title=bar
[Bot] Updated tag with name "spam".
---------------------------------
[Alkali] !tag edit --response=POTATO SALAD
[Bot] Missing argument. ("name")
---------------------------------
[Alkali] !tag modify --name=foo --embed=true --title=Well hello there
[Bot] Updated tag with name "foo".
```

</br>

### Setup

This command allows a guild to be setup with custom commands, using the [default configuration](#example-config "Example Configuration") setup

> **Syntax:** `{Command Prefix}tag setup`

Examples:
```
[Alkali] !tag setup
[Bot] 
```

</br>

### List

This returns a list of all tags you have access to. (Both Guild and Global level) Though if you are incapable of running the tag there is an asterisk (`*`) before it.

> **Syntax:** `{Command Prefix}tag setup`

Examples:
```
[Alkali] !tag list
[Bot] Tags list: "*alkali, potato, spam, *foo"
```

</br>

-------------------------------------------

</br>

<a id="example-config"></a>

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