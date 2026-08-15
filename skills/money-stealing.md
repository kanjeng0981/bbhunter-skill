---
name: money-stealing
description: Financial logic flaws — rounding, currency, and balance manipulation
scope: web2
---
Money / financial flaw testing checklist:

1. Test rounding errors: values that produce fractional units rounded in the
   user's favor (round-down bugs).
2. Manipulate currency: switch currency mid-transaction, exploit conversion
   rates, use negative or zero amounts.
3. Test balance/points double-spend via race conditions or parallel requests.
4. Manipulate price fields in requests (client-side price trust).
5. Test refund/cancel flows for creating money (cancel after credit).
6. Check voucher/gift-card redemption reuse.
7. On web3 targets: inspect token transfer/balance logic for manipulation.

## References

- Round error produces free money on a Bitcoin site — https://hackerone.com/reports/176461
- Manipulation of ETH balance — https://www.vicompany.nl/magazine/from-christmas-present-in-the-blockchain-to-massive-bug-bounty
