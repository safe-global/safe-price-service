import gevent
from gunicorn.workers.ggevent import GeventWorker


class MyGeventWorker(GeventWorker):
    def patch_psycopg2(self) -> bool:
        try:
            from psycogreen.gevent import patch_psycopg

            patch_psycopg()
            self.log.info("Patched Psycopg2 for gevent")
            return True
        except ImportError:
            self.log.info("Cannot patch psycopg2 for gevent, install psycogreen")
            return False

    def patch(self):
        super().patch()
        self.log.info("Patched all for gevent")
        self.patch_psycopg2()

    def handle_request(self, listener_name, req, sock, addr):
        try:
            with gevent.Timeout(self.cfg.timeout):
                super().handle_request(listener_name, req, sock, addr)
        except gevent.Timeout:
            self.log.error("TimeoutError on %s", req.path)
