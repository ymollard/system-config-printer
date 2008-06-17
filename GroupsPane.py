import gobject
import gtk
from gettext import gettext as _

class GroupsPane:
    def __init__ (self, treeview):
        self.list_store = None
        self.current_search_iter = None
        self.selection = None

        self.list_store = gtk.ListStore (gtk.gdk.Pixbuf,
                                         gobject.TYPE_STRING)
        treeview.set_model (self.list_store)
        tvcolumn = gtk.TreeViewColumn ()
        treeview.append_column (tvcolumn)
        pixbuf_cell = gtk.CellRendererPixbuf ()
        text_cell = gtk.CellRendererText ()
        tvcolumn.pack_start (pixbuf_cell, False)
        tvcolumn.pack_start (text_cell, False)
        tvcolumn.add_attribute (pixbuf_cell, 'pixbuf', 0)
        tvcolumn.add_attribute (text_cell, 'markup', 1)

        theme = gtk.icon_theme_get_default ()
        try:
            pixbuf = theme.load_icon ('gnome-dev-printer',
                                      gtk.ICON_SIZE_MENU, 0)
        except gobject.GError:
            pixbuf = None

        iter = self.list_store.append (row = [pixbuf, _("All Printers")])

        self.selection = treeview.get_selection ()
        self.selection.select_iter (iter)

    def add_current_search (self):
        if self.current_search_iter == None:
            self.current_search_iter = self.list_store.append (
                row = [None, _("<i>Current search</i>")])
            self.selection.select_iter (self.current_search_iter)

    def remove_current_search (self):
        if self.current_search_iter != None:
            self.list_store.remove (self.current_search_iter)
            self.current_search_iter = None
            self.selection.select_iter (self.list_store.get_iter_first ())
