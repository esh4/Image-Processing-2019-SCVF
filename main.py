from scvf import cv_loop
from scvf import io
from hatch_pipeline import GripPipeline as HatchPipeline

def main():
    nt_io = io.NetworkTableIO('10.59.90.2', 'ImageProcessing')
    piplines = {'hatch': HatchPipeline()}

    cv_loop.start(piplines, camera_port=1, output_consumer=nt_io.output_consumer, settings_supplier=nt_io.settings_supplier)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        cv_loop.end()

if __name__ == '__main__':
    main()