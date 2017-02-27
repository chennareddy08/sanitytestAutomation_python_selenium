
import webbrowser as m

class MyTransaction(object):

    def run(self):
        br = m()
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(m._http.HTTPRefreshProcessor(),max_time=1)
        _ = br.open('http://reddit.tlys.us')
        br.select_form(nr=1)
        br.form['user'] = u
        br.form['passwd'] = p
        r = br.submit()
        r.read()