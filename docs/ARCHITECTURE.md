# Architecture

The system keeps the last confirmed image in the active slot while a new image is staged in the inactive slot. A boot manager owns active/pending selection, boot-attempt counting, confirmation, and rollback.
