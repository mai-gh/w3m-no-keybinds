# w3m-no-keybinds: NO PRESET KEYBINDS in w3m

---

w3m lets you change keybinds, but it doesn't let you unset any. The defaults are always reverted back to if there is a hiccup with your overrides.

w3m has many cool features, but I only want a just a few at "normal" key combos. w3m is old, from an era before "normal" browser key combos. This PKGBUILD just adds a some manipulation of `./src/w3m/keybind.c` to set every hard coded keybind to `nulcmd` with the exception of `escbmap` and `escmap` as they seem to be required for some non-ascii keys to work (arrow keys, F1-12, etc).

After you build and install this, you will have not keybinds mapped! You will need to copy over `/usr/share/doc/w3m/keymap.default` to `~/.w3m/keymap` and then you will now have the default keys set up. Now with the bonus of being able to comment out the ones you dont want ;-)
