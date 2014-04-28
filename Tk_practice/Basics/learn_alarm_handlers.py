"""
                Alarm Handlers:
                ---------------

Basics:
-------

Methods that let us peform some periodic actions are called alarm handlers.
Some commonly used Tkinter alarm handlers include:

1. after(delay_ms, callback, args...)

- Registers an alarm callback to the called after given number of milliseconds

2. after_cancel(id)

- Cancels the given alarm callback

3. after_idle(callback, args...)

- Calls back only when there are no more events to process in the mainloop,
that is, after the system becomes idle.
"""
