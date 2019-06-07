<?php
// ディレクトリのパス
$dir = "img/" ;

if( is_dir( $dir ) && $handle = opendir( $dir ) ) {
	while( ($file = readdir($handle)) !== false ) {
		if( filetype( $path = $dir . $file ) == "file" ) {
			// $file: ファイル名
			// $path: ファイルのパス
			echo file;
		}
	}
}
?>
