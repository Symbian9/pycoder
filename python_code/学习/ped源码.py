# emacs-mode: -*- python-*-
__version__ = '2.15 final'
import sys
import e32
import os
import ui
symbols = [('()',
  1),
 ('[]',
  1),
 ('{}',
  1),
 ("''",
  1)]
statements = [('____',
  2),
 ('break',
  None),
 ('class :',
  6),
 ('class ():',
  6),
 ('class (object):',
  6),
 ('continue',
  None),
 ('def ():',
  4),
 ('def (self):',
  4),
 ('elif :',
  5),
 ('else:',
  None),
 ('except:',
  None),
 ('finally:',
  None),
 ('for  in :',
  4),
 ('from  import *',
  5),
 ('global ',
  None),
 ('if :',
  3),
 ('import ',
  None),
 ('lambda :',
  7),
 ('pass',
  None),
 ('print ',
  None),
 ('return',
  None),
 ('try:',
  None),
 ('while :',
  6)]
class Window(ui.Window):
    __module__ = __name__
    root_menu = ui.Menu()

    def __init__(self, *args, **kwargs):
        ui.Window.__init__(self, *args, **kwargs)
        menu = self.root_menu.copy()
        self.init_menu(menu)
        self.menu = menu



    def init_menu(self, menu):
        pass


    def focus_changed(self, focus):
        if focus:
            wnds_item = self.menu.find(u'\u7a97\u53e3 ')
            if wnds_item:
                wnds_item.submenu = ui.screen.get_windows_menu()
                wnds_item.submenu.sort()
                wnds_item.hidden = (not len(wnds_item.submenu))
                self.update_menu()



    def close(self):
        r = ui.Window.close(self)
        if r:
            self.menu = ui.Menu()
        return r



class TextWindow(Window):
    __module__ = __name__
    settings = {}

    def __init__(self, *args, **kwargs):
        Window.__init__(self, *args, **kwargs)
        self.body = ui.Text()
        self.find_text = u''
        self.keys += [ui.EKeyEnter,
         ui.EKeySelect]
        self.control_keys += [ui.EKey3,
         ui.EKey6,
         ui.EKey2,
         ui.EKey4,
         ui.EKey7,
         ui.EKeyLeftArrow,
         ui.EKeyRightArrow,
         ui.EKeyUpArrow,
         ui.EKeyDownArrow,
         ui.EKeyEdit]
        self.apply_settings()



    def init_menu(self, menu):
        file_item = menu.find(u'\u6587\u4ef6')
        if (not file_item):
            return 
        edit_menu = ui.Menu()
        edit_menu.append(ui.MenuItem(u'\u627e\u67e5', target=self.find_click))
        edit_menu.append(ui.MenuItem(u'\u627e\u67e5\u4e0b\u4e00\u4e2a', target=self.findnext_click))
        edit_menu.append(ui.MenuItem(u'\u627e\u67e5\u5168\u90e8', target=self.findall_click))
        edit_menu.append(ui.MenuItem(u'\u8f6c\u5230...\u884c', target=self.gotoline_click))
        edit_menu.append(ui.MenuItem(u'\u9876\u90e8', target=self.move_beg_of_document))
        edit_menu.append(ui.MenuItem(u'\u5e95\u90e8', target=self.move_end_of_document))
        edit_menu.append(ui.MenuItem(u'\u5168\u5c4f', target=self.fullscreen_click))
        i = menu.index(file_item)
        menu.insert((i + 1), ui.MenuItem(u'\u7f16\u8f91', submenu=edit_menu))



    def enter_key_press(self):
        pass


    def key_press(self, key):
        if (key == ui.EKeySelect):
            self.body.add(u'\n')
            ui.schedule(self.enter_key_press)
            return True
        elif (key == ui.EKeyEnter):
            ui.schedule(self.enter_key_press)
            return True
        return Window.key_press(self, key)



    def control_key_press(self, key):
        if (key == ui.EKey3):
            self.find_click()
            return True
        elif (key == ui.EKey6):
            self.findnext_click()
            return True
        elif (key == ui.EKey2):
            self.findall_click()
            return True
        elif (key == ui.EKey4):
            self.gotoline_click()
            return True
        elif (key == ui.EKey7):
            self.fullscreen_click()
            return True
        elif (key == ui.EKeyEdit):
            item = self.menu.find(u'\u7f16\u8f91').submenu.popup()
            if item:
                item.target()
        elif (key == ui.EKeyLeftArrow):
            self.move_beg_of_line(1)
        elif (key == ui.EKeyRightArrow):
            self.move_end_of_line(-1)
        elif (key == ui.EKeyUpArrow):
            self.move_page_up(1)
        elif (key == ui.EKeyDownArrow):
            self.move_page_down(-1)
        else:
            return Window.control_key_press(self, key)
        return False



    def apply_settings(self, font = 'font', color = 'color'):
        do = False
        try:
            value = self.settings[font].get()
            if (self.body.font != value):
                self.body.font = value
                do = True
        except KeyError:
            pass
        try:
            value = self.settings[color].get()
            if (self.body.color != value):
                self.body.color = value
                do = True
        except KeyError:
            pass
        if do:
            pos = self.body.get_pos()
            self.body.set(self.body.get())
            self.body.set_pos(pos)



    def update_settings(cls):
        fwin = ui.screen.focused_window()
        if fwin:
            fwin.focus = False
        for win in ui.screen.windows:
            if isinstance(win, TextWindow):
                win.apply_settings()

        if fwin:
            fwin.focus = True


    update_settings = classmethod(update_settings)

    def get_lines(self):
        lines = []
        pos = 0
        n = 1
        for line in self.body.get().split(u'\u2029'):
            lines.append((n,
             pos,
             line))
            n += 1
            pos += (len(line) + 1)

        return lines



    def get_line_from_pos(self, pos = None, lines = None):
        if (pos == None):
            pos = self.body.get_pos()
        if (lines == None):
            lines = self.get_lines()
        for (ln, lpos, line,) in lines:
            if lpos <= pos <= (lpos + len(line)):
                break

        return (ln,
         lpos,
         line)



    def find_click(self):
        find_text = ui.query(u'Find:', 'text', self.find_text)
        if find_text:
            self.find_text = find_text
            self.findnext_click(False)



    def findnext_click(self, skip = True):
        find_text = self.find_text.lower()
        if (not find_text):
            self.find_click()
            return 
        text = self.body.get().lower()
        i = self.body.get_pos()
        while True:
            pos = i
            if (skip and (text[i:(i + len(find_text))] == find_text)):
                i += len(find_text)
            i = text.find(find_text, i)
            if (i >= 0):
                self.body.set_pos(i)
            elif (pos != 0):
                if ui.query(u'Not found, start from beginning?', 'query'):
                    i = 0
                    skip = False
                    continue
            else:
                ui.note(u'Not found')
            break




    def findall_click(self):
        find_text = ui.query(u'Find All:', 'text', self.find_text)
        if find_text:
            self.find_text = find_text
            find_text = find_text.lower()
            results = []
            for (ln, lpos, line,) in self.get_lines():
                pos = 0
                while 1:
                    pos = line.lower().find(find_text, pos)
                    if (pos < 0):
                        break
                    results.append((ln,
                     lpos,
                     line,
                     pos))
                    pos += len(find_text)


            if results:
                win = ui.screen.create_window(FindResultsWindow, title=('Find: %s' % find_text), results=results)
                line = win.modal(self)
                if line:
                    self.body.set_pos((line[1] + line[3]))
            else:
                ui.note(u'Not found')



    def gotoline_click(self):
        lines = self.get_lines()
        ln = self.get_line_from_pos(lines=lines)[0]
        ln = ui.query((u'Line (1-%d):' % len(lines)), 'number', ln)
        if (ln != None):
            if (ln < 1):
                ln = 1
            ln -= 1
            try:
                self.body.set_pos(lines[ln][1])
            except IndexError:
                self.body.set_pos(self.body.len())



    def move_beg_of_line(self, delta = 0):
        self.body.set_pos((self.get_line_from_pos()[1] + delta))



    def move_end_of_line(self, delta = 0):
        line = self.get_line_from_pos()
        self.body.set_pos(((line[1] + len(line[2])) + delta))



    def move_page_up(self, delta = 0):
        lines = self.get_lines()
        i = (((self.get_line_from_pos(lines=lines)[0] - 1) - self.settings['pagesize'].get()) + delta)
        if (i < 0):
            i = 0
        self.body.set_pos(lines[i][1])



    def move_page_down(self, delta = 0):
        lines = self.get_lines()
        i = (((self.get_line_from_pos(lines=lines)[0] - 1) + self.settings['pagesize'].get()) + delta)
        if (i >= len(lines)):
            i = -1
        self.body.set_pos(lines[i][1])



    def move_beg_of_document(self):
        self.body.set_pos(0)



    def move_end_of_document(self):
        self.body.set_pos(self.body.len())



    def fullscreen_click(self):
        if (self.size == ui.sizNormal):
            self.size = ui.sizLarge
        else:
            self.size = ui.sizNormal



class FindResultsWindow(Window):
    __module__ = __name__

    def __init__(self, *args, **kwargs):
        if ('title' not in kwargs):
            kwargs['title'] = 'Find All'
        Window.__init__(self, *args, **kwargs)
        self.results = kwargs['results']
        self.body = ui.Listbox([ ((u'Line %d, Column %d' % (x[0],
          x[3])),
         x[2]) for x in self.results ], self.select_click)
        self.menu = ui.Menu()
        self.menu.append(ui.MenuItem(u'\u9009\u62e9', target=self.select_click))
        self.menu.append(ui.MenuItem(u'\u9000\u51fa', target=self.close))



    def close(self):
        r = Window.close(self)
        if r:
            self.menu = ui.Menu()
        return r



    def select_click(self):
        self.modal_result = self.results[self.body.current()]
        self.close()



class TextFileWindow(TextWindow):
    __module__ = __name__
    type_name = 'Text'
    type_ext = '.txt'
    session = ui.Settings('')

    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, *args, **kwargs)
        try:
            self.path = kwargs['path']
            (text, self.encoding,) = self.load()
            self.fixed_encoding = True
            self.body.set(text)
            self.body.set_pos(0)
            self.title = os.path.split(self.path)[1].decode('utf8')
        except KeyError:
            self.path = None
            self.fixed_encoding = False
            self.encoding = 'latin1'
        self.autosave_timer = e32.Ao_timer()
        self.apply_settings()



    def apply_settings(self, font = 'font', color = 'color', defenc = 'defenc', autosave = 'autosave'):
        TextWindow.apply_settings(self, font, color)
        try:
            if (not self.fixed_encoding):
                self.encoding = self.settings[defenc].get()
            autosave = self.settings[autosave].get()
            self.autosave_timer.cancel()
            if (autosave and (self.path != None)):
                self.autosave_timer.after(autosave, self.save)
        except AttributeError:
            pass



    def can_close(self):
        if (not TextWindow.can_close(self)):
            return False
        text = self.body.get()
        if (self.path == None):
            if (not text):
                return True
        else:
            try:
                if (text == self.load()[0]):
                    return True
            except IOError:
                pass
        if ui.query(u'\u4fdd\u5b58\u6587\u4ef6\u5417', 'query'):
            return self.save()
        elif ui.query(u'\u786e\u5b9a\u8981\u5173\u95ed', 'query'):
            return True
        return False



    def close(self):
        if TextWindow.close(self):
            self.autosave_timer.cancel()
            return True
        return False



    def init_menu(self, menu):
        TextWindow.init_menu(self, menu)
        file_menu = menu.find(u'\u6587\u4ef6').submenu
        file_menu.append(ui.MenuItem(u'\u4fdd\u5b58', target=self.save))
        file_menu.append(ui.MenuItem(u'\u53e6\u5b58\u4e3a', target=self.save_as))
        file_menu.append(ui.MenuItem(u'\u5168\u90e8\u4fdd\u5b58', target=self.save_all))
        file_menu.append(ui.MenuItem(u'\u5173\u95ed', target=self.close))
        file_menu.append(ui.MenuItem(u'\u5168\u90e8\u5173\u95ed', target=self.close_all))



    def load(self):
        if (self.path == None):
            raise IOError('TextFileWindow: no path specified')
        f = file(self.path, 'r')
        text = f.read()
        f.close()
        if (text.startswith('\xff\xfe') or text.startswith('\xfe\xff')):
            enc = 'utf16'
            text = text.decode(enc)
        else:
            for enc in ['utf8',
             'latin1']:
                try:
                    text = text.decode(enc)
                    break
                except UnicodeError:
                    pass
            else:
                raise UnicodeError

        return (text.replace(u'\r\n', u'\u2029').replace(u'\n', u'\u2029'),
         enc)



    def save(self):
        if (self.path == None):
            return self.save_as()
        autosave = self.settings['autosave'].get()
        self.autosave_timer.cancel()
        if autosave:
            self.autosave_timer.after(autosave, self.save)
        try:
            f = file(self.path, 'w')
            f.write(self.body.get().replace(u'\u2029', u'\r\n').encode(self.encoding))
            f.close()
            return True
        except IOError:
            ui.note(u'Cannot save file!', 'error')
            return False



    def save_as(self):
        path = self.path
        if (path == None):
            path = self.title.encode('utf8')
        win = ui.screen.create_window(ui.FileBrowserWindow, mode=ui.fbmSave, path=path, title='Save file')
        path = win.modal(self)
        if (path == None):
            return False
        self.path = path
        self.title = os.path.split(path)[1].decode('utf8')
        return self.save()



    def close_all(self):
        for win in ui.screen.find_windows(TextFileWindow):
            if (not win.close()):
                return 




    def save_all(self):
        for win in ui.screen.find_windows(TextFileWindow):
            if (not win.save()):
                return 




    def store_session(cls):
        state = cls.session['state'].get()
        state.clear()
        for win in ui.screen.find_windows(TextFileWindow):
            try:
                text = win.body.get()
                encoding = win.encoding
                if (win.load()[0] == text):
                    text = None
                else:
                    raise IOError
            except IOError:
                pass
            if win.path:
                path = win.path
            else:
                path = win.title.encode('utf8')
            state[path] = (text,
             encoding)

        cls.session.save()


    store_session = classmethod(store_session)

    def clear_session(cls):
        cls.session['state'].get().clear()
        cls.session.save()


    clear_session = classmethod(clear_session)

class PythonModifier(object):
    __module__ = __name__
    py_namespace = {}

    def py_reset_namespace(cls):
        import __main__
        cls.py_namespace.clear()
        cls.py_namespace.update(__main__.__dict__)
        cls.py_namespace.update(__main__.__builtins__.__dict__)
        cls.py_namespace['__name__'] = '__main__'


    py_reset_namespace = classmethod(py_reset_namespace)

    def _get_text(self):
        return (self.body.get(),
         self.body.get_pos())



    def _get_objects(self, name):
        s = name.split('.')
        n = '.'.join(s[:-1])
        e = s[-1]
        if (n == ''):
            d = filter(lambda x:x.startswith(e)
, eval('dir()', self.py_namespace))
            try:
                return dict([ (x,
                 eval('.'.join((s[:-1] + [x])), self.py_namespace)) for x in d ])
            except:
                pass
        else:
            namespace = sys.modules.copy()
            namespace.update(self.py_namespace)
            try:
                d = filter(lambda x:x.startswith(e)
, eval(('dir(%s)' % n), namespace))
                return dict([ (x,
                 eval('.'.join((s[:-1] + [x])), namespace)) for x in d ])
            except:
                pass
        return {}



    def _get_object(self, name):
        d = self._get_objects(name)
        try:
            return d[name.split('.')[-1]]
        except:
            pass



    def py_insert_indent(self):
        (text, pos,) = self._get_text()
        pos -= 1
        i = (pos - 1)
        while (i >= 0):
            if (text[i] == u'\u2029'):
                break
            i -= 1

        i += 1
        strt = i
        while ((i < pos) and text[i].isspace()):
            i += 1

        ind = (i - strt)
        if ((pos > 0) and (text[(pos - 1)] == u':')):
            ind += self.settings['indent'].get()
        self.body.add((u' ' * ind))



    def py_autocomplete(self):
        (text, pos,) = self._get_text()
        epos = pos
        spos = (pos - 1)
        while (spos >= 0):
            if (not (text[spos].isalnum() or (text[spos] in u'._'))):
                break
            spos -= 1

        spos += 1
        name = text[spos:pos]
        menu = ui.Menu(('%s*' % name))
        menu.items += [ ui.MenuItem(title) for title in self._get_objects(name).keys() ]
        menu.items += [ ui.MenuItem(title, offset=off) for (title, off,) in filter(lambda x:x[0].startswith(name)
, statements) ]
        menu.sort()
        symbitems = [ ui.MenuItem(title, offset=off) for (title, off,) in symbols ]
        if name:
            menu.items += symbitems
        else:
            menu.items = (symbitems + menu.items)
        item = menu.popup(full_screen=True, search_field=True)
        if item:
            while (epos < self.body.len()):
                if (not (text[epos].isalnum() or (text[epos] in u'._'))):
                    break
                epos += 1

            if (epos > pos):
                self.body.delete(pos, (epos - pos))
                self.body.set_pos(pos)
            ws = s = item.title
            n = name.split(u'.')[-1]
            if s.startswith(n):
                s = s[len(n):]
            self.body.add(s)
            if hasattr(item, 'offset'):
                if (item.offset != None):
                    self.body.set_pos(((self.body.get_pos() - len(ws)) + item.offset))



    def py_calltip(self):
        stdhelp = u'\u8bf7\u5c06\u5149\u6807\u79fb\u81f3\u51fd\u6570\u7684\u5706\u62ec\u53f7\u5185'
        (text, pos,) = self._get_text()
        pos -= 1
        lev = 0
        while (pos >= 0):
            if (text[pos] == u'('):
                lev -= 1
                if (lev < 0):
                    break
            elif (text[pos] == u')'):
                lev += 1
            pos -= 1
        else:
            ui.note(stdhelp)
            return 

        while (pos >= 0):
            if (not text[pos].isspace()):
                break
            pos -= 1
        else:
            ui.note(stdhelp)
            return 

        i = pos
        pos -= 1
        while (pos >= 0):
            if (not (text[pos].isalnum() or (text[pos] in u'._'))):
                break
            pos -= 1

        name = text[(pos + 1):i]
        if name:
            win = ui.screen.create_window(TextWindow, title=u'\u67e5\u770b\u8c03\u7528')
            menu = ui.Menu()
            menu.append(ui.MenuItem(u'\u5173\u95ed', target=win.close))
            win.menu = menu
            obj = self._get_object(name)
            if (obj != None):
                import types
                argoffset = 0
                arg_text = ''
                if (type(obj) in (types.ClassType,
                 types.TypeType)):

                    def find_init(obj):
                        try:
                            return obj.__init__.im_func
                        except AttributeError:
                            for base in obj.__bases__:
                                fob = find_init(base)
                                if (fob != None):
                                    return None



                    fob = find_init(obj)
                    if (fob == None):
                        fob = lambda :None

                    else:
                        argoffset = 1
                elif (type(obj) == types.MethodType):
                    fob = obj.im_func
                    argoffset = 1
                else:
                    fob = obj
                if (type(fob) in (types.FunctionType,
                 types.LambdaType)):
                    try:
                        real_args = fob.func_code.co_varnames[argoffset:fob.func_code.co_argcount]
                        defaults = (fob.func_defaults or [])
                        defaults = list([ ('=%s' % repr(x)) for x in defaults ])
                        defaults = (([''] * (len(real_args) - len(defaults))) + defaults)
                        items = map(lambda arg, dflt:(arg + dflt)
, real_args, defaults)
                        if (fob.func_code.co_flags & 4):
                            items.append('...')
                        if (fob.func_code.co_flags & 8):
                            items.append('***')
                        arg_text = ('%s(%s)' % (name,
                         ', '.join(items)))
                    except:
                        pass
                doc = getattr(obj, '__doc__', '')
                if doc:
                    while (doc[:1] in ' \t\n'):
                        doc = doc[1:]

                    if (not arg_text):
                        arg_text = name
                    arg_text += ('\n\n' + doc)
                if arg_text:
                    win.body.add((unicode(arg_text) + u'\n'))
                else:
                    win.body.add((u'%s()\n\nNo additional info available.\n' % name))
            else:
                win.body.add((u'%s\n\nUnknown object.\n' % name))
            win.focus = True
        else:
            ui.note(stdhelp)



PythonModifier.py_reset_namespace()
class PythonFileWindow(TextFileWindow,
 PythonModifier):
    __module__ = __name__
    type_name = 'Python'
    type_ext = '.py'

    def __init__(self, *args, **kwargs):
        TextFileWindow.__init__(self, *args, **kwargs)
        PythonModifier.__init__(self)
        self.control_keys += [ui.EKey5,
         ui.EKeySelect,
         ui.EKey0]



    def init_menu(self, menu):
        TextFileWindow.init_menu(self, menu)
        menu.insert(0, ui.MenuItem(u'\u8fd0\u884c', target=self.run_click))
        edit_menu = menu.find(u'\u7f16\u8f91').submenu
        i = edit_menu.index(edit_menu.find(u'\u9876\u90e8'))
        edit_menu.insert(i, ui.MenuItem(u'\u51fd\u6570\u5217\u8868', target=self.codebrowser_click))
        edit_menu.insert((i + 1), ui.MenuItem(u'\u67e5\u770b\u8c03\u7528', target=self.py_calltip))



    def enter_key_press(self):
        TextFileWindow.enter_key_press(self)
        self.py_insert_indent()



    def control_key_press(self, key):
        if (key == ui.EKey5):
            ui.schedule(self.py_calltip)
            return True
        elif (key == ui.EKeySelect):
            self.py_autocomplete()
        elif (key == ui.EKey0):
            self.codebrowser_click()
            return True
        else:
            return TextFileWindow.control_key_press(self, key)
        return False



    def run_click(self):
        TextFileWindow.store_session()
        try:
            if (self.load()[0] == self.body.get()):
                path = self.path
            else:
                raise IOError
        except IOError:
            dirpath = 'D:\\Ped.temp'
            if (not os.path.exists(dirpath)):
                try:
                    os.mkdir(dirpath)
                except OSError:
                    dirpath = 'D:\\'
            path = os.path.join(dirpath, self.title.encode('utf8'))
            try:
                f = file(path, 'w')
                f.write(self.body.get().replace(u'\u2029', u'\r\n').encode(self.encoding))
                f.close()
            except IOError, (errno, errstr,):
                ui.note(unicode(errstr), 'error')
                return 
        shell = StdIOWrapper.shell()
        shell.restart()
        shell.enable_prompt(False)
        shell.lock(True)
        ui.app.menu = []
        ui.app.exit_key_handler = ui.screen.close
        mysys = (list(sys.argv),
         list(sys.path))
        sys.path.insert(0, os.path.split(path)[0])
        sys.argv = [path]
        try:
            execfile(path, self.py_namespace)
        except:
            (value, traceback_,) = sys.exc_info()[1:]
            import traceback
            traceback.print_exc()
            e = traceback.extract_tb(traceback_)[-1]
            if (e[0] != path):
                s = ('(%s, line ' % os.path.split(path)[1])
                value = str(value)
                pos = value.find(s, 0)
                if (pos >= 0):
                    value = value[(pos + len(s)):]
                    self.goto_error(int(value[:value.index(')')]))
            else:
                self.goto_error(e[1], unicode(e[3]))
            del traceback_
        (sys.argv, sys.path,) = mysys
        shell.lock(False)
        ui.screen.redraw()
        shell.enable_prompt(True)
        TextFileWindow.clear_session()

        def remove(name):
            if os.path.isdir(name):
                for item in os.listdir(name):
                    remove(os.path.join(name, item))

                os.rmdir(name)
            else:
                os.remove(name)


        remove('D:\\Ped.temp')



    def goto_error(self, lineno, text = None):
        (ln, pos, line,) = self.get_lines()[(lineno - 1)]
        if text:
            c = line.find(text)
            if (c > 0):
                pos += c
        self.body.set_pos(pos)



    def codebrowser_click(self):
        tree = self.parse_code()

        def tree_to_menu(tree, title = None):
            if (title == None):
                t = u'\u51fd\u6570\u5217\u8868'
            else:
                t = title
            menu = ui.Menu(t)
            for e in tree:
                if e.endswith(u'()'):
                    menu.append(ui.MenuItem(e, pos=tree[e][0]))
                    name = e[:-2]
                else:
                    name = e[:-1]
                if len(tree[e][1]):
                    if (title == None):
                        t = name
                    else:
                        t = ((title + u'.') + name)
                    menu.append(ui.MenuItem((name + u'.'), submenu=tree_to_menu(tree[e][1], t)))

            menu.sort()
            return menu


        item = tree_to_menu(tree).popup(full_screen=True, search_field=True)
        if item:
            self.body.set_pos(item.pos)



    def parse_code(self):
        lines = self.get_lines()
        end = {'class': '.',
         'def': '()'}
        last = root = {}
        lev = [(0,
          root)]
        off = 0
        for (lnum, lpos, ln,) in lines:
            coff = off
            off += (len(ln) + 1)
            ln = ln.rstrip()
            t = ln.lstrip()
            if ((t == u'') or (t[0] == u'#')):
                continue
            ind = ln.find(t[0])
            t = t.split()
            if (ind < lev[-1][0]):
                try:
                    while (ind < lev[-1][0]):
                        lev.pop()

                except IndexError:
                    return 
            elif (ind > lev[-1][0]):
                lev.append((ind,
                 last))
            if (t[0] in (u'class',
             u'def')):
                tok = t[1].split(u'(')[0].split(u':')[0]
                name = (tok + end[t[0]])
                if (name in lev[-1][1]):
                    name = (u'%s/%d%s' % (tok,
                     (coff + ind),
                     end[t[0]]))
                last = {}
                lev[-1][1][name] = ((coff + ind),
                 last)

        return root



class IOWindow(TextWindow):
    __module__ = __name__

    def __init__(self, *args, **kwargs):
        TextWindow.__init__(self, *args, **kwargs)
        self.control_keys += [ui.EKeyBackspace]
        self.event = None
        self.locked = None
        self.write_buf = []

        def make_flusher(body, buf):

            def doflush():
                ln = body.len()
                if (body.get_pos() != ln):
                    body.set_pos(ln)
                body.add(u''.join(buf))
                del buf[:]
                ln = body.len()
                if (ln > 3000):
                    body.delete(0, (ln - 250))


            return doflush


        self.do_flush = make_flusher(self.body, self.write_buf)
        self.flush_gate = e32.ao_callgate(self.do_flush)



    def control_key_press(self, key):
        if (key == ui.EKeyBackspace):
            if (self.locked == False):
                self.locked = True
            return True
        else:
            return TextWindow.control_key_press(self, key)



    def enter_key_press(self):
        if self.event:
            self.event.set()
            return True
        TextWindow.enter_key_press(self)
        return False



    def can_close(self):
        if self.event:
            self.input_aborted = True
            self.write('\n')
            self.event.set()
            return False
        if (self.locked == False):
            self.locked = True
            return False
        return TextWindow.can_close(self)



    def close(self):
        r = TextWindow.close(self)
        if r:
            del self.flush_gate
        return r



    def lock(self, enable):
        if enable:
            self.locked = False
        else:
            self.locked = None



    def is_locked(self):
        return (self.locked != None)



    def readline(self, size = None):
        if (not e32.is_ui_thread()):
            raise IOError('IOWindow.readline() called from non-UI thread')
        self.input_aborted = False
        self.event = ui.Event()
        input_pos = self.body.get_pos()
        while (not self.event.isSet()):
            self.event.wait()
            if ((not self.input_aborted) and (self.body.get_pos() < input_pos)):
                ln = self.body.len()
                self.body.set_pos(ln)
                if (input_pos > ln):
                    input_pos = self.body.get_pos()
                continue
            break

        self.event = None
        if self.input_aborted:
            raise EOFError
        text = (self.body.get(input_pos).split(u'\u2029')[0].encode('latin-1', 'replace') + '\n')
        self.body.set_pos(self.body.len())
        if (size and (len(text) > size)):
            text = text[:size]
        return text



    def write(self, s):
        self.write_buf.append(unicode(s))
        self.flush()



    def writelines(self, lines):
        self.write_buf += map(unicode, lines)
        self.flush()



    def flush(self):
        if self.write_buf:
            if e32.is_ui_thread():
                self.do_flush()
            else:
                self.flush_gate()
        if (self.locked == True):
            self.locked = False
            raise KeyboardInterrupt



class PythonShellWindow(IOWindow,
 PythonModifier):
    __module__ = __name__

    def __init__(self, *args, **kwargs):
        if ('title' not in kwargs):
            kwargs['title'] = u'\u547d\u4ee4\u884c\u6a21\u5f0f'
        IOWindow.__init__(self, *args, **kwargs)
        PythonModifier.__init__(self)
        self.control_keys += [ui.EKeyUpArrow,
         ui.EKeyDownArrow,
         ui.EKeyBackspace,
         ui.EKeyLeftArrow,
         ui.EKey5,
         ui.EKeySelect]
        self.old_stdio = (sys.stdin,
         sys.stdout,
         sys.stderr)
        sys.stdin = sys.stdout = sys.stderr = self
        self.write(('Python %s on %s\nType "copyright", "credits" or "license" for more information.\nPed %s\n' % (sys.version,
         sys.platform,
         __version__)))
        self.prompt_enabled = True
        self.init_console()
        self.prompt()



    def init_console(self):
        from code import InteractiveConsole
        self.console = InteractiveConsole(locals=self.py_namespace)
        self.history = [(u'import btconsole; btconsole.main()')]
        self.history_ptr = len(self.history)
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = '>>> '



    def restart(self):
        PythonModifier.py_reset_namespace()
        try:
            del self.py_namespace['_']
        except KeyError:
            pass
        self.init_console()
        halfbar = ('=' * 5)
        self.write((((halfbar + ' RESTART ') + halfbar) + '\n'))
        self.prompt()



    def close(self):
        r = IOWindow.close(self)
        if r:
            (sys.stdin, sys.stdout, sys.stderr,) = self.old_stdio
        return r



    def init_menu(self, menu):
        IOWindow.init_menu(self, menu)
        menu.insert(0, ui.MenuItem(u'\u5386\u53f2\u547d\u4ee4', target=self.history_click))
        file_menu = menu.find(u'\u6587\u4ef6').submenu
        file_menu.append(ui.MenuItem(u'\u4fdd\u5b58\u5230...', target=self.export_click))
        edit_menu = menu.find(u'\u7f16\u8f91').submenu
        i = edit_menu.index(edit_menu.find(u'\u9876\u90e8'))
        edit_menu.insert(i, ui.MenuItem(u'\u67e5\u770b\u8c03\u7528', target=self.py_calltip))
        edit_menu.insert((i + 1), ui.MenuItem(u'\u6e05\u9664', target=self.clear_click))



    def control_key_press(self, key):
        if (key in (ui.EKeyUpArrow,
         ui.EKeyDownArrow)):
            if (key == ui.EKeyUpArrow):
                if (self.history_ptr > 0):
                    self.history_ptr -= 1
                else:
                    ui.schedule(self.body.set_pos, self.body.get_pos())
                    return False
            elif (self.history_ptr < len(self.history)):
                self.history_ptr += 1
            else:
                ui.schedule(self.body.set_pos, self.body.get_pos())
                return False
            try:
                statement = self.history[self.history_ptr]
                self.body.delete(self.prompt_pos)
                self.body.set_pos(self.prompt_pos)
                self.write('\n'.join(statement))
                ui.schedule(self.body.set_pos, self.body.get_pos())
            except IndexError:
                self.body.delete(self.prompt_pos)
                ui.schedule(self.body.set_pos, self.prompt_pos)
        elif (key == ui.EKeyLeftArrow):
            (ln, pos, line,) = self.get_line_from_pos()
            if pos <= self.prompt_pos <= (pos + len(line)):
                pos = self.prompt_pos
            ui.schedule(self.body.set_pos, pos)
        elif (key == ui.EKeyBackspace):
            if (not self.is_locked()):
                pos = self.body.get_pos()
                if (pos >= self.prompt_pos):
                    if (pos == self.prompt_pos):
                        self.body.add(u' ')
                    if (self.body.len() > self.prompt_pos):

                        def clear():
                            self.body.delete(self.prompt_pos)
                            self.body.set_pos(self.prompt_pos)


                        ui.schedule(clear)
            else:
                return IOWindow.control_key_press(self, key)
        elif (key == ui.EKey5):
            ui.schedule(self.py_calltip)
            return True
        elif (key == ui.EKeySelect):
            self.py_autocomplete()
        else:
            return IOWindow.control_key_press(self, key)
        return False



    def enable_prompt(self, enable):
        enabled = self.prompt_enabled
        self.prompt_enabled = bool(enable)
        if ((not enabled) and enable):
            self.prompt()
        elif (enabled and (not enable)):
            self.write('\n')



    def prompt(self):
        if (not self.prompt_enabled):
            return 
        try:
            self.write(str(sys.ps1))
        except:
            pass
        self.prompt_pos = self.body.get_pos()
        self.statement = []



    def enter_key_press(self):
        if IOWindow.enter_key_press(self):
            return 
        if self.is_locked():
            return 
        pos = self.body.get_pos()
        if ((pos > 0) and (self.body.get((pos - 1), 1) == u'\u2029')):
            self.body.delete((pos - 1), 1)
            pos -= 1
        if (pos < self.prompt_pos):
            self.body.set_pos(self.body.len())
            if (self.body.get_pos() < self.prompt_pos):
                self.write('\n')
                self.prompt()
            line = self.get_line_from_pos(pos=pos)[2]
            try:
                if line.startswith(str(sys.ps1)):
                    line = line[len(str(sys.ps1)):]
            except:
                pass
            self.write(line)
            return 
        if (self.body.get(pos).find(u'\u2029') >= 0):
            self.write('\n')
            self.py_insert_indent()
            return 
        self.body.set_pos(self.body.len())
        statement = self.body.get(self.prompt_pos).split(u'\u2029')
        self.write('\n')
        statement = (filter(lambda line:bool(line.strip())
, statement[:-1]) + statement[-1:])
        self.lock(True)
        try:
            self.console.resetbuffer()
            more = False
            for line in statement:
                if line.strip():
                    s = line
                else:
                    s = ''
                if (not self.console.push(s)):
                    break
            else:
                self.py_insert_indent()
                return 

            if (statement[0] and (self.history[-1] != tuple(statement))):
                self.history.append(tuple(statement))
            self.history_ptr = len(self.history)
            self.prompt()

        finally:
            self.lock(False)




    def apply_settings(self, font = 'font', color = 'shellcolor'):
        IOWindow.apply_settings(self, font, color)



    def history_click(self):
        win = ui.screen.create_window(HistoryWindow, history=self.history, ptr=self.history_ptr)
        ptr = win.modal(self)
        if (ptr != None):
            self.history_ptr = ptr
            statement = self.history[ptr]
            self.body.delete(self.prompt_pos)
            self.body.set_pos(self.prompt_pos)
            self.write('\n'.join(statement))



    def export_click(self):
        win = ui.screen.create_window(ui.FileBrowserWindow, mode=ui.fbmSave, path='PythonShell.txt', title=u'\u4fdd\u5b58\u6587\u4ef6\u523d')
        path = win.modal(self)
        if (path == None):
            return 
        try:
            f = file(path, 'w')
            f.write(self.body.get().replace(u'\u2029', u'\r\n').encode(self.settings['defenc'].get()))
            f.close()
        except IOError:
            ui.note(u'Cannot export the output!', 'error')



    def clear_click(self):
        if ui.query(u'\u6e05\u9664\u9875\u9762', 'query'):
            self.body.clear()
            self.prompt()



class HistoryWindow(Window):
    __module__ = __name__

    def __init__(self, *args, **kwargs):
        if ('title' not in kwargs):
            kwargs['title'] = u'\u5386\u53f2\u547d\u4ee4'
        Window.__init__(self, *args, **kwargs)
        self.history = kwargs['history']
        try:
            ptr = kwargs['ptr']
        except KeyError:
            ptr = 0
        self.body = ui.Listbox([u''], self.select_click)
        self.body.set_list([ '; '.join(filter(bool, [ y.strip() for y in x ])).replace(':;', ':') for x in self.history ], ptr)
        self.menu = ui.Menu()
        self.menu.append(ui.MenuItem(u'\u9009\u62e9', target=self.select_click))
        self.menu.append(ui.MenuItem(u'\u9000\u51fa', target=self.close))



    def close(self):
        r = Window.close(self)
        if r:
            self.menu = ui.Menu()
        return r



    def select_click(self):
        self.modal_result = self.body.current()
        self.close()



class HelpWindow(TextWindow):
    __module__ = __name__

    def __init__(self, *args, **kwargs):
        if ('title' not in kwargs):
            kwargs['title'] = u'\u5e2e\u52a9'
        TextWindow.__init__(self, *args, **kwargs)
        f = file(kwargs['path'], 'r')
        text = f.read()
        f.close()
        if (text.startswith('\xff\xfe') or text.startswith('\xfe\xff')):
            text = text.decode('utf16')
        else:
            for enc in ['utf8',
             'latin1']:
                try:
                    text = text.decode(enc)
                    break
                except UnicodeError:
                    pass
            else:
                raise UnicodeError

        self.body.set(text.replace(u'\r\n', u'\u2029').replace(u'\n', u'\u2029'))
        self.body.set_pos(0)



    def init_menu(self, menu):
        TextWindow.init_menu(self, menu)
        menu.insert(0, ui.MenuItem('Topic List', target=self.topics_click))



    def topics_click(self):

        def istopic((ln, lpos, line,)):
            i = line.find(u' ')
            if (i < 0):
                return False
            for c in line[:i]:
                if (not (c.isdigit() or (c == u'.'))):
                    return False

            return True


        menu = ui.Menu('Topic List')
        for (ln, lpos, topic,) in filter(istopic, self.get_lines()):
            menu.append(ui.MenuItem(topic, line=ln, pos=lpos))

        item = menu.popup(search_field=True)
        if item:
            self.body.set_pos(item.pos)



class StdIOWrapper(object):
    __module__ = __name__
    singleton = None

    def __init__(self):
        if (self.singleton != None):
            raise AssertionError('only one instance of StdIOWrapper allowed')
        self.win = None
        StdIOWrapper.singleton = self



    def shell(cls):
        self = cls.singleton
        if (not self):
            raise AssertionError('StdIOWrapper must be instatinated first')
        if (self.win and self.win.is_alive()):
            self.win.focus = True
            return self.win
        try:
            ui.screen.open_blank_window()
            self.win = ui.screen.create_window(PythonShellWindow)
            self.win.focus = True
            return self.win
        except:
            import traceback
            ui.app.title = u'\u53d1\u751f\u9519\u8bef'
            ui.app.screen = 'normal'
            ui.app.focus = None
            ui.app.body = ui.Text()
            lock = e32.Ao_lock()
            ui.app.exit_key_handler = lock.signal
            ui.app.menu = [(u'\u9000\u51fa',
              lock.signal)]
            ui.app.body.set(unicode(''.join(traceback.format_exception(*sys.exc_info()))))
            lock.wait()
            ui.screen.redraw()
            raise 


    shell = classmethod(shell)

    def readline(self, size = None):
        return self.shell().readline(size)



    def write(self, s):
        return self.shell().write(s)



    def writelines(self, lines):
        return self.shell().writelines(lines)



file_windows_types = [TextFileWindow,
 PythonFileWindow]
class Application(object):
    __module__ = __name__

    def __init__(self):
        self.path = os.path.split(sys.argv[0])[0]
        allfonts = ui.available_text_fonts()
        if (u'LatinBold12' in allfonts):
            defaultfont = u'LatinBold12'
        else:
            defaultfont = allfonts[0]
        allcolors = ((u'\u9ed1\u8272',
          0),
         (u'\u7ea2\u8272',
          10027008),
         (u'\u7eff\u8272',
          34816),
         (u'\u84dd\u8272',
          153),
         (u'\u7d2b\u8272',
          10027161))
        allorientations = [(u'\u81ea\u52a8',
          ui.oriAutomatic)]
        if (e32.s60_version_info >= (3,
         0)):
            allorientations += [('Portrait',
              ui.oriPortrait),
             ('Landscape',
              ui.oriLandscape)]
        settings = ui.Settings(os.path.join(self.path, 'settings.bin'))
        settings.category = u'\u754c\u9762'
        settings.add('font', ui.ComboSetting(u'\u5b57\u4f53', defaultfont, allfonts))
        settings.add('color', ui.ValueComboSetting(u'\u7f16\u8f91\u754c\u9762\u989c\u8272', u'\u84dd\u8272', allcolors))
        settings.add('shellcolor', ui.ValueComboSetting(u'\u547d\u4ee4\u754c\u9762\u989c\u8272', u'\u7eff\u8272', allcolors))
        settings.add('orientation', ui.ValueComboSetting(u'\u65b9\u5411', allorientations[0][0], allorientations))
        settings.category = u'\u6587\u672c'
        settings.add('pagesize', ui.NumberSetting(u'\u7ffb\u9875\u5927\u5c0f', 8, vmin=1, vmax=32))
        settings.add('indent', ui.NumberSetting(u'\u7f29\u8fdb\u5927\u5c0f', 4, vmin=1, vmax=8))
        settings.category = u'\u6587\u4ef6'
        settings.add('defenc', ui.ComboSetting(u'\u7f16\u7801', 'utf-8', ('ascii',
         'latin-1',
         'utf-8',
         'utf-16')))
        settings.add('autosave', ui.ValueComboSetting(u'\u81ea\u52a8\u4fdd\u5b58', u'\u5173', ((u'\u5173',
          0),
         (u'30\u79d2\u949f',
          30),
         (u'1 \u5206\u949f',
          60),
         (u'2 \u5206\u949f',
          120),
         (u'5 \u5206\u949f',
          300),
         (u'10\u5206\u949f',
          600))))
        settings.load_if_available()
        self.settings = TextWindow.settings = settings
        self.apply_settings()
        ui.FileBrowserWindow.icons_file = os.path.join(self.path, 'file_browser_icons.mbm')
        ui.FileBrowserWindow.add_link('C:\\Python')
        ui.FileBrowserWindow.add_link('E:\\Python')
        if (not ui.FileBrowserWindow.add_link('E:\\System\\Apps\\Python', u'\u547d\u4ee4\u884c\u6a21\u5f0f')):
            ui.FileBrowserWindow.add_link('C:\\System\\Apps\\Python', u'\u547d\u4ee4\u884c\u6a21\u5f0f')
        session = ui.Settings(os.path.join(self.path, 'session.bin'))
        session.add('state', ui.Setting('Files', {}))
        session.load_if_available()
        TextFileWindow.session = session
        self.settings_win = self.browser_win = self.help_win = None
        self.unnamed_count = 1
        file_menu = ui.Menu()
        file_menu.append(ui.MenuItem(u'\u65b0\u5efa', target=self.new_click))
        file_menu.append(ui.MenuItem(u'\u6253\u5f00 ', target=self.open_click))
        main_menu = ui.Menu()
        main_menu.append(ui.MenuItem(u'\u6587\u4ef6', submenu=file_menu))
        main_menu.append(ui.MenuItem(u'\u7a97\u53e3 ', submenu=ui.Menu(), hidden=True))
        main_menu.append(ui.MenuItem(u'\u547d\u4ee4\u884c\u6a21\u5f0f', target=StdIOWrapper.shell))
        main_menu.append(ui.MenuItem(u'\u8fd0\u884c\u811a\u672c', target=self.runscript_click))
        main_menu.append(ui.MenuItem(u'\u8bbe\u7f6e  ', target=self.settings_click))
        main_menu.append(ui.MenuItem(u'\u5e2e\u52a9', target=self.help_click))
        main_menu.append(ui.MenuItem(u'\u9000\u51fa', target=ui.screen.close))
        Window.root_menu = main_menu
        state = session['state'].get()
        if (state and ui.query(u'Last Ped session crashed. Reload its last state?', 'query')):
            for (path, (text, encoding,),) in state.items():
                if (text == None):
                    self.load_file(path)
                else:
                    ext = os.path.splitext(path)[1].lower()
                    try:
                        klass = file_windows_types[[ x.type_ext.lower() for x in file_windows_types ].index(ext)]
                    except ValueError:
                        klass = TextFileWindow
                    ui.screen.open_blank_window()
                    win = ui.screen.create_window(klass, title=os.path.split(path)[1].decode('utf8'))
                    if win:
                        win.body.set(text)
                        win.body.set_pos(0)
                        win.encoding = encoding
                        if os.path.split(path)[0]:
                            win.path = path
                            win.fixed_encoding = True
                        else:
                            win.fixed_encoding = False
                        win.focus = True

        state.clear()
        try:
            session.save()
        except IOError:
            ui.note(u'Cannot update session file!', 'error')



    def start(self):
        self.old_stdio = (sys.stdin,
         sys.stdout,
         sys.stderr)
        sys.stdin = sys.stdout = sys.stderr = StdIOWrapper()
        for path in ('C:\\Python\\lib',
         'E:\\Python\\lib'):
            if os.path.exists(path):
                sys.path.append(path)

        ui.screen.close_handler = self.close_handler
        ui.screen.menu = Window.root_menu.copy()
        menu = ui.Menu(u'\u6587\u4ef6')
        menu.append(ui.MenuItem(u'\u6253\u5f00 ', target=self.open_click))

        def make_target(klass):
            return lambda :self.new_file(klass)



        for klass in file_windows_types:
            menu.append(ui.MenuItem(('New ' + klass.type_name), target=make_target(klass)))

        ui.screen.popup_menu = menu
        ui.screen.bkgnd_redraw_callback = self.bkgnd_redraw_callback



    def bkgnd_redraw_callback(self, body, size, coords):
        white = 16777215
        f = 'dense'
        space = 8
        m = body.measure_text(u'A', font=f)[0]
        h = (m[3] - m[1])
        (x, y,) = (10,
         (10 + h))
        body.text((x,
         y), u'\u98de\u5f717610\u6c49\u5316', fill=white, font=f)
        y += space
        body.line((x,
         y,
         (size[0] - x),
         y), outline=white)
        y += (space + h)
        body.text((x,
         y), (u'Version: %s' % __version__), fill=white, font=f)
        y += (space + h)
        body.text((x,
         y), (u'Python for S60: %s' % e32.pys60_version), fill=white, font=f)



    def new_file(self, klass):
        title = ('Unnamed%d%s' % (self.unnamed_count,
         klass.type_ext))
        self.unnamed_count += 1
        win = ui.screen.create_window(klass, title=title)
        win.focus = True



    def settings_click(self):
        if self.settings_win:
            self.settings_win.focus = True
            return 
        self.settings_win = ui.screen.create_window(ui.SettingsWindow, settings=self.settings)
        r = self.settings_win.modal()
        self.settings_win = None
        if r:
            self.apply_settings()



    def apply_settings(self):
        TextWindow.update_settings()
        ui.screen.orientation = self.settings['orientation'].get()



    def help_click(self):
        if (self.help_win and self.help_win.is_alive()):
            self.help_win.focus = True
            return 
        wwin = ui.screen.open_blank_window()
        try:
            self.help_win = ui.screen.create_window(HelpWindow, path=os.path.join(self.path, 'help.txt'))
            self.help_win.body.add((u'Ped %s\n\nCopyright \xa9 2007\nArkadiusz Wahlig\n<yak@nokix.pasjagsm.pl>\n\n' % __version__))
            self.help_win.body.set_pos(0)
            self.help_win.focus = True
        except IOError:
            ui.note(u'Cannot load help file!', 'error')
            wwin.close()



    def close_handler(self):
        (sys.stdin, sys.stdout, sys.stderr,) = self.old_stdio
        ui.app.set_exit()



    def new_click(self):
        menu = ui.Menu(u'\u65b0\u5efa')
        for klass in file_windows_types:
            menu.append(ui.MenuItem(klass.type_name, klass=klass))

        item = menu.popup()
        if item:
            self.new_file(item.klass)



    def open_click(self):
        if self.browser_win:
            ui.note(u'File browser already in use!', 'error')
            return 
        self.browser_win = ui.screen.create_window(ui.FileBrowserWindow, title=u'\u6253\u5f00\u6587\u4ef6')
        path = self.browser_win.modal()
        self.browser_win = None
        if (not path):
            return 
        self.load_file(path)



    def load_file(self, path):
        for win in ui.screen.find_windows(TextFileWindow):
            if (win.path == path):
                win.focus = True
                return 

        ext = os.path.splitext(path)[1].lower()
        try:
            klass = file_windows_types[[ x.type_ext.lower() for x in file_windows_types ].index(ext)]
        except ValueError:
            klass = TextFileWindow
        wwin = ui.screen.open_blank_window()
        try:
            win = ui.screen.create_window(klass, path=path)
            win.focus = True
        except IOError:
            ui.note((u'Cannot load %s file!' % os.path.split(path)[1]), 'error')
            wwin.close()
        return win



    def runscript_click(self):
        if self.browser_win:
            ui.note(u'File browser already in use!', 'error')
            return 
        self.browser_win = ui.screen.create_window(ui.FileBrowserWindow, title='Open script')
        path = self.browser_win.modal()
        self.browser_win = None
        if (not path):
            return 
        shell = StdIOWrapper.shell()
        shell.restart()
        shell.enable_prompt(False)
        shell.lock(True)
        TextFileWindow.store_session()
        ui.app.menu = []
        ui.app.exit_key_handler = ui.screen.close
        mysys = (list(sys.argv),
         list(sys.path))
        sys.path.insert(0, os.path.split(path)[0])
        sys.argv = [path]
        try:
            execfile(path, shell.py_namespace)

        finally:
            (sys.argv, sys.path,) = mysys
            TextFileWindow.clear_session()
            shell.lock(False)
            ui.screen.redraw()
            shell.enable_prompt(True)




    def windows_click(self):
        pass



# local variables:
# tab-width: 4
