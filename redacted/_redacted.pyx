

cdef class SecretContainer:
    cdef object secret
    cdef public unsigned int locked

    property secret:
        def __get__(self):
            if not self.locked:
                return self.secret

            raise ValueError("can't access locked secrets")

        def __set__(self, value):
            if not self.locked:
                self.secret = value
            else:
                raise ValueError("can't modify locked secrets")
