module tech.altier.personalizedfitnessrecommendersystemfrontend {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;

    requires com.dlsc.formsfx;
    requires net.synedra.validatorfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires eu.hansolo.tilesfx;

    opens tech.altier.personalizedfitnessrecommendersystemfrontend to javafx.fxml;
    exports tech.altier.personalizedfitnessrecommendersystemfrontend;
}