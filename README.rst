dploy-cargo-tools - Collection of tools for dploy's cargo
=========================================================

This is a collection of tools meant to be used inside of an LXC. They are
designed specifically for the dploy system. 

The tools are the following:

- ``dploy-crash-notify`` - A supervisor event handling script that notifies a
  dploy zone of a crash.
- ``dploy-cargo-builder`` - A startup script that runs the building process for
  dploy cargo.
- ``dploy-interactive`` - A script that interacts with other scripts. This is
  meant for one-off processes run within dploy cargo.
