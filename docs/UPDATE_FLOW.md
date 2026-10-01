# Update Flow

1. Receive image metadata.
2. Check minimum-version policy.
3. Select inactive slot.
4. Install the candidate image.
5. Mark it pending.
6. Boot the pending slot.
7. Wait for application confirmation.
8. Promote confirmed slot to active; otherwise rollback after the attempt limit.
