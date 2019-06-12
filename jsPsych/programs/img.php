<?php
	// ディレクトリのパス
	$dir = "img/" ;

	if( is_dir( $dir ) && $handle = opendir( $dir ) ) {
		while( ($file = readdir($handle)) !== false ) {
			if( filetype( $path = $dir . $file ) == "file" ) {
				// $file: ファイル名
				// $path: ファイルのパス
			}
		}
	}

	$files = array();
	foreach(glob($dir . '*png') as $file){
		array_push($files, $file);
	}
	var_dump($files);
?>
