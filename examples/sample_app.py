"""A synthetic order application used to demonstrate repository inspection."""
import decimal


def total(prices):
    """Calculate a Decimal order total."""
    return sum((decimal.Decimal(str(p)) for p in prices), decimal.Decimal(0))


class Checkout:
    def invoice(self, prices):
        """Return a simple invoice payload."""
        return {"amount": str(total(prices))}


async def health():
    return {"status": "ok"}
