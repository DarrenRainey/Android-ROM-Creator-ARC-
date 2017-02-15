cd ~/android/system
source build/envsetup.sh
breakfast hammerhead
cd ~/android/system/device/lge/hammerhead
echo "Please Connect Your Nexus 5"

function pause(){
   read -p "$*"
}

pause 'Press [Enter] key to continue...'
# rest of the script
export ANDROID_JACK_VM_ARGS="-Dfile.encoding=UTF-8 -XX:+TieredCompilation -Xmx4G"
croot
brunch hammerhead
cd $OUT
echo Build Complete
ls