from ... import exc

class AsyncMethodRequired(exc.InvalidRequestError): ...
class AsyncContextNotStarted(exc.InvalidRequestError): ...
class AsyncContextAlreadyStarted(exc.InvalidRequestError): ...
