from krita import DockWidgetFactory, DockWidgetFactoryBase
from .krita_connect import krita_connect


Application.addDockWidgetFactory(
    DockWidgetFactory("Krita Connect",
                      DockWidgetFactoryBase.DockRight,
                      krita_connect))
