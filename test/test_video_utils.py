
import unittest
import os
import cv_basic_utils as cbu


class TestVideoUtils(unittest.TestCase):
    def test_h265write(self): # test h265write
        width, height, n_frames, fps = 1344, 756, 50, 25  # 50 frames, resolution 1344x756, and 25 fps

        output_filename = 'output.mp4'

        cap = H265Writer(output_filename, fps, width, height)

        # Build synthetic video frames and write them to ffmpeg input stream.
        for i in range(n_frames):
            # Build synthetic image for testing ("render" a video frame).
            img = np.full((height, width, 3), 60, np.uint8)
            cv2.putText(img, str(i+1), (width//2-100*len(str(i+1)), height//2+100), cv2.FONT_HERSHEY_DUPLEX, 10, (255, 30, 30), 20)  # Blue number

            # Write raw video frame to input stream of ffmpeg sub-process.
            cap.write(img)

        cap.close()

        # Check if output file exists
        self.assertTrue(os.path.isfile(output_filename))

