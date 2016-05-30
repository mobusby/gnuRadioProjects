#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Commercial FM
# Generated: Sun May 29 20:14:42 2016
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import osmosdr
import sip
import sys

from distutils.version import StrictVersion
class osmoCommercialFM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Commercial FM")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Commercial FM")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "osmoCommercialFM")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.volume_slider = volume_slider = 5
        self.samp_rate_slider = samp_rate_slider = 2.0
        self.freq_slider = freq_slider = 92.9
        self.filter_transition_slider = filter_transition_slider = 20
        self.filter_cutoff_slider = filter_cutoff_slider = 80
        self.volume = volume = volume_slider
        self.samp_rate = samp_rate = samp_rate_slider * 1e6
        self.quadrature_slider = quadrature_slider = 400
        self.freq = freq = freq_slider * 1e6
        self.filter_transition = filter_transition = filter_transition_slider * 1e3
        self.filter_decimation = filter_decimation = 1
        self.filter_cutoff = filter_cutoff = filter_cutoff_slider * 1e3
        self.audio_feed_rate = audio_feed_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_slider_layout = Qt.QVBoxLayout()
        self._volume_slider_label = Qt.QLabel("Volume")
        self._volume_slider_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider_slider.setRange(0, 30, 1)
        self._volume_slider_slider.setValue(self.volume_slider)
        self._volume_slider_slider.setMinimumWidth(30)
        self._volume_slider_slider.valueChanged.connect(self.set_volume_slider)
        self._volume_slider_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._volume_slider_layout.addWidget(self._volume_slider_label)
        self._volume_slider_layout.addWidget(self._volume_slider_slider)
        self.top_grid_layout.addLayout(self._volume_slider_layout, 0,0)
        self._samp_rate_slider_layout = Qt.QVBoxLayout()
        self._samp_rate_slider_tool_bar = Qt.QToolBar(self)
        self._samp_rate_slider_layout.addWidget(self._samp_rate_slider_tool_bar)
        self._samp_rate_slider_tool_bar.addWidget(Qt.QLabel("Sample Rate [MHz]"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._samp_rate_slider_counter = qwt_counter_pyslot()
        self._samp_rate_slider_counter.setRange(1.0, 2.5, 0.1)
        self._samp_rate_slider_counter.setNumButtons(2)
        self._samp_rate_slider_counter.setValue(self.samp_rate_slider)
        self._samp_rate_slider_tool_bar.addWidget(self._samp_rate_slider_counter)
        self._samp_rate_slider_counter.valueChanged.connect(self.set_samp_rate_slider)
        self._samp_rate_slider_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._samp_rate_slider_slider.setRange(1.0, 2.5, 0.1)
        self._samp_rate_slider_slider.setValue(self.samp_rate_slider)
        self._samp_rate_slider_slider.setMinimumWidth(250)
        self._samp_rate_slider_slider.valueChanged.connect(self.set_samp_rate_slider)
        self._samp_rate_slider_layout.addWidget(self._samp_rate_slider_slider)
        self.top_grid_layout.addLayout(self._samp_rate_slider_layout, 1,1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(audio_feed_rate),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self._quadrature_slider_layout = Qt.QHBoxLayout()
        self._quadrature_slider_layout.addWidget(Qt.QLabel("quadrature [KHz]"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._quadrature_slider_counter = qwt_counter_pyslot()
        self._quadrature_slider_counter.setRange(1, 1000, 1)
        self._quadrature_slider_counter.setNumButtons(2)
        self._quadrature_slider_counter.setMinimumWidth(1000)
        self._quadrature_slider_counter.setValue(self.quadrature_slider)
        self._quadrature_slider_layout.addWidget(self._quadrature_slider_counter)
        self._quadrature_slider_counter.valueChanged.connect(self.set_quadrature_slider)
        self.top_grid_layout.addLayout(self._quadrature_slider_layout, 1,0)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"Filtered", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-160, 10)
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 5,0,1,3)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"Raw", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, 10)
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 4,0,1,3)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(filter_decimation, firdes.low_pass(
        	1, samp_rate, filter_cutoff, filter_transition, firdes.WIN_HAMMING, 6.76))
        self._freq_slider_layout = Qt.QVBoxLayout()
        self._freq_slider_tool_bar = Qt.QToolBar(self)
        self._freq_slider_layout.addWidget(self._freq_slider_tool_bar)
        self._freq_slider_tool_bar.addWidget(Qt.QLabel("Frequency [MHz]"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._freq_slider_counter = qwt_counter_pyslot()
        self._freq_slider_counter.setRange(88.1, 107.9, .2)
        self._freq_slider_counter.setNumButtons(2)
        self._freq_slider_counter.setValue(self.freq_slider)
        self._freq_slider_tool_bar.addWidget(self._freq_slider_counter)
        self._freq_slider_counter.valueChanged.connect(self.set_freq_slider)
        self._freq_slider_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_slider_slider.setRange(88.1, 107.9, .2)
        self._freq_slider_slider.setValue(self.freq_slider)
        self._freq_slider_slider.setMinimumWidth(200)
        self._freq_slider_slider.valueChanged.connect(self.set_freq_slider)
        self._freq_slider_layout.addWidget(self._freq_slider_slider)
        self.top_grid_layout.addLayout(self._freq_slider_layout, 0,1)
        self._filter_transition_slider_layout = Qt.QVBoxLayout()
        self._filter_transition_slider_tool_bar = Qt.QToolBar(self)
        self._filter_transition_slider_layout.addWidget(self._filter_transition_slider_tool_bar)
        self._filter_transition_slider_tool_bar.addWidget(Qt.QLabel("Filter Transition [KHz]"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._filter_transition_slider_counter = qwt_counter_pyslot()
        self._filter_transition_slider_counter.setRange(1, 500, 1)
        self._filter_transition_slider_counter.setNumButtons(2)
        self._filter_transition_slider_counter.setValue(self.filter_transition_slider)
        self._filter_transition_slider_tool_bar.addWidget(self._filter_transition_slider_counter)
        self._filter_transition_slider_counter.valueChanged.connect(self.set_filter_transition_slider)
        self._filter_transition_slider_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._filter_transition_slider_slider.setRange(1, 500, 1)
        self._filter_transition_slider_slider.setValue(self.filter_transition_slider)
        self._filter_transition_slider_slider.setMinimumWidth(500)
        self._filter_transition_slider_slider.valueChanged.connect(self.set_filter_transition_slider)
        self._filter_transition_slider_layout.addWidget(self._filter_transition_slider_slider)
        self.top_grid_layout.addLayout(self._filter_transition_slider_layout, 2,1)
        self._filter_cutoff_slider_layout = Qt.QVBoxLayout()
        self._filter_cutoff_slider_tool_bar = Qt.QToolBar(self)
        self._filter_cutoff_slider_layout.addWidget(self._filter_cutoff_slider_tool_bar)
        self._filter_cutoff_slider_tool_bar.addWidget(Qt.QLabel("Filter Cutoff [KHz]"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._filter_cutoff_slider_counter = qwt_counter_pyslot()
        self._filter_cutoff_slider_counter.setRange(1, 500, 1)
        self._filter_cutoff_slider_counter.setNumButtons(2)
        self._filter_cutoff_slider_counter.setValue(self.filter_cutoff_slider)
        self._filter_cutoff_slider_tool_bar.addWidget(self._filter_cutoff_slider_counter)
        self._filter_cutoff_slider_counter.valueChanged.connect(self.set_filter_cutoff_slider)
        self._filter_cutoff_slider_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._filter_cutoff_slider_slider.setRange(1, 500, 1)
        self._filter_cutoff_slider_slider.setValue(self.filter_cutoff_slider)
        self._filter_cutoff_slider_slider.setMinimumWidth(500)
        self._filter_cutoff_slider_slider.valueChanged.connect(self.set_filter_cutoff_slider)
        self._filter_cutoff_slider_layout.addWidget(self._filter_cutoff_slider_slider)
        self.top_grid_layout.addLayout(self._filter_cutoff_slider_layout, 2,0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(int(audio_feed_rate), "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "osmoCommercialFM")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume_slider(self):
        return self.volume_slider

    def set_volume_slider(self, volume_slider):
        self.volume_slider = volume_slider
        self.set_volume(self.volume_slider)
        Qt.QMetaObject.invokeMethod(self._volume_slider_slider, "setValue", Qt.Q_ARG("double", self.volume_slider))

    def get_samp_rate_slider(self):
        return self.samp_rate_slider

    def set_samp_rate_slider(self, samp_rate_slider):
        self.samp_rate_slider = samp_rate_slider
        self.set_samp_rate(self.samp_rate_slider * 1e6)
        Qt.QMetaObject.invokeMethod(self._samp_rate_slider_counter, "setValue", Qt.Q_ARG("double", self.samp_rate_slider))
        Qt.QMetaObject.invokeMethod(self._samp_rate_slider_slider, "setValue", Qt.Q_ARG("double", self.samp_rate_slider))

    def get_freq_slider(self):
        return self.freq_slider

    def set_freq_slider(self, freq_slider):
        self.freq_slider = freq_slider
        self.set_freq(self.freq_slider * 1e6)
        Qt.QMetaObject.invokeMethod(self._freq_slider_counter, "setValue", Qt.Q_ARG("double", self.freq_slider))
        Qt.QMetaObject.invokeMethod(self._freq_slider_slider, "setValue", Qt.Q_ARG("double", self.freq_slider))

    def get_filter_transition_slider(self):
        return self.filter_transition_slider

    def set_filter_transition_slider(self, filter_transition_slider):
        self.filter_transition_slider = filter_transition_slider
        self.set_filter_transition(self.filter_transition_slider * 1e3)
        Qt.QMetaObject.invokeMethod(self._filter_transition_slider_counter, "setValue", Qt.Q_ARG("double", self.filter_transition_slider))
        Qt.QMetaObject.invokeMethod(self._filter_transition_slider_slider, "setValue", Qt.Q_ARG("double", self.filter_transition_slider))

    def get_filter_cutoff_slider(self):
        return self.filter_cutoff_slider

    def set_filter_cutoff_slider(self, filter_cutoff_slider):
        self.filter_cutoff_slider = filter_cutoff_slider
        self.set_filter_cutoff(self.filter_cutoff_slider * 1e3)
        Qt.QMetaObject.invokeMethod(self._filter_cutoff_slider_counter, "setValue", Qt.Q_ARG("double", self.filter_cutoff_slider))
        Qt.QMetaObject.invokeMethod(self._filter_cutoff_slider_slider, "setValue", Qt.Q_ARG("double", self.filter_cutoff_slider))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_cutoff, self.filter_transition, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.freq, self.samp_rate)

    def get_quadrature_slider(self):
        return self.quadrature_slider

    def set_quadrature_slider(self, quadrature_slider):
        self.quadrature_slider = quadrature_slider
        Qt.QMetaObject.invokeMethod(self._quadrature_slider_counter, "setValue", Qt.Q_ARG("double", self.quadrature_slider))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.freq, self.samp_rate)

    def get_filter_transition(self):
        return self.filter_transition

    def set_filter_transition(self, filter_transition):
        self.filter_transition = filter_transition
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_cutoff, self.filter_transition, firdes.WIN_HAMMING, 6.76))

    def get_filter_decimation(self):
        return self.filter_decimation

    def set_filter_decimation(self, filter_decimation):
        self.filter_decimation = filter_decimation

    def get_filter_cutoff(self):
        return self.filter_cutoff

    def set_filter_cutoff(self, filter_cutoff):
        self.filter_cutoff = filter_cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_cutoff, self.filter_transition, firdes.WIN_HAMMING, 6.76))

    def get_audio_feed_rate(self):
        return self.audio_feed_rate

    def set_audio_feed_rate(self, audio_feed_rate):
        self.audio_feed_rate = audio_feed_rate

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = osmoCommercialFM()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
