# Automated Voiceless Roles


## Overview

This plugin allows users to receive a role when they connect to a voice channel (this keeps in mind the server verification level as well) so that they can get special permissions to do stuff when in a voice channel. You can have a default role for all channels, or can specify what role goes to specifically what channel, this allows you to have a different role assigned if the user joins a different voice channel.

</br>

-------------------------------------------

</br>

## Commands

### Setup

This is the first command that must be ran in order for the guild to be set up in the plugin's configuration, this will enable the other commands after being ran. These commands can **ONLY** be ran by users who possess the `Manage Channels` permission.

> **Syntax:** `{Command Prefix}voiceless setup`

Examples:
```
[Alkali] !voiceless setup
[Bot] Guild has been set up to use automated voiceless roles!
```

</br>
</br>

### Set

This command allows creating and changing the role mappings for voiceless channels, this enables you to not have any role for a specific channel, not have a role for any channel unless the channel overrides it. The heirarchy order for checking for giving out roles is channel specific and then if it doesn't find any mapping for that channel it will fallback to default. (Which can be set to `None`) This command can also only be ran by people who have the `Manage Channels` permission.

> **Syntax:** `{Command Prefix}voiceless set <Channel> <Role>`
>
> * `<Channel>` must be a name or an ID prefaced by `id:`, if using a name, you must replace spaces with a `+`.
>   * Ex: `id:12345678987654321`, `General+Voice+Chat`
> * `<Role>` must be a name, ID, or role mention. Same rules apply as the channel, if using a name, you must replace spaces with a `+` if using a role mention, this can be ignored, if using an ID, it must be prefaced with `id:`.

Examples:
```
[Alkali] !voiceless set The+Room+Where+It+Happens @TheRoomWhereItDoesn'tHappen
[Bot] `CHANNEL ID`'s role mapping changed to: `ROLE ID`
---------------------------------
[Alkali] !voiceless set The+Room+Where+It+Happens --none
[Bot] `CHANNEL ID`'s role mapping has been removed. (Set to `None`)
---------------------------------
[Alkali] !voiceless set -default The+Room+Where+It+Doesn't+Happen
[Bot] Default role mapping changed to: `ROLE ID`
---------------------------------
[Alkali] !voiceless set -default --none
[Bot] Default role mapping removed. (Set to `None`)
```

</br>
</br>

### Delete

Removes a custom role mapping from a channel, makes it revert to the default mapping. The role mapping will also be removed automatically if the channel is deleted from the guild itself.

> **Syntax:** `{Command Prefix}voiceless delete <Channel>`
>
>* `<Channel>` must be a name or an ID prefaced by `id:`, if using a name, you must replace spaces with a `+`.
>   * Ex: `id:12345678987654321`, `General+Voice+Chat`

Examples:
```
[1-3 examples]
```

</br>

-------------------------------------------

</br>

## Example Configuration

Configuration Name: `voiceless_role_mappings.json`

This config has commands to be edited from within the Discord client, but must be created in the route directory for all of the configs (`data/` by default) in order for the commands to work. Otherwise it will throw an exit error when you try to run a command.

```json
{
  "GUILD ID HERE": {
    "default": null
  },
  "ANOTHER GUILD ID HERE": {
    "default": ROLE ID HERE,
    "CHANNEL ID HERE": null
  },
  "A THIRD GUILD ID HERE": {
    "default": null,
    "ANOTHER CHANNEL ID HERE": ANOTHER ROLE ID HERE,
    "A THIRD CHANNEL ID HERE": A THIRD ROLE ID HERE
  }
}
```