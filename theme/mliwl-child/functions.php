<?php
/**
 * MLIWL child theme for Hello Elementor.
 *
 * Loads the brand font, the design tokens (generated from Figma) and the
 * component classes that editors apply through Elementor's "CSS Classes" field.
 *
 * @package mliwl
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'MLIWL_THEME_VERSION', '0.1.0' );

/**
 * Enqueue parent theme, Montserrat and the MLIWL stylesheets.
 *
 * Tokens load first so components.css (and any Elementor custom CSS) can use them.
 */
function mliwl_enqueue_styles() {
	$uri = get_stylesheet_directory_uri() . '/assets/css/';

	wp_enqueue_style( 'hello-elementor', get_template_directory_uri() . '/style.css', array(), MLIWL_THEME_VERSION );

	wp_enqueue_style(
		'mliwl-font',
		'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;800;900&display=swap',
		array(),
		null
	);

	wp_enqueue_style( 'mliwl-tokens', $uri . 'tokens.css', array( 'hello-elementor' ), MLIWL_THEME_VERSION );
	wp_enqueue_style( 'mliwl-components', $uri . 'components.css', array( 'mliwl-tokens', 'mliwl-font' ), MLIWL_THEME_VERSION );
}
add_action( 'wp_enqueue_scripts', 'mliwl_enqueue_styles', 20 );

/**
 * Mobile menu: the header's Menu button opens the "MLIWL Mobile Menu" popup.
 * Finds the popup by its title so no ID has to be typed in after importing.
 */
function mliwl_enqueue_mobile_menu() {
	$popups = get_posts(
		array(
			'post_type'      => 'elementor_library',
			'title'          => 'MLIWL Mobile Menu',
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
		)
	);
	if ( empty( $popups ) ) {
		return;
	}
	wp_enqueue_script( 'mliwl-mobile-menu', get_stylesheet_directory_uri() . '/assets/js/mobile-menu.js', array( 'jquery' ), MLIWL_THEME_VERSION, true );
	wp_localize_script( 'mliwl-mobile-menu', 'mliwlMenu', array( 'popupId' => (int) $popups[0] ) );
}
add_action( 'wp_enqueue_scripts', 'mliwl_enqueue_mobile_menu', 30 );

/**
 * Same styles inside the Elementor editor preview, so editors see the real result.
 */
add_action( 'elementor/preview/enqueue_styles', 'mliwl_enqueue_styles' );

/**
 * Preconnect to Google Fonts for a faster first paint.
 *
 * @param array  $urls          URLs to print for resource hints.
 * @param string $relation_type The relation type the URLs are printed for.
 * @return array
 */
function mliwl_resource_hints( $urls, $relation_type ) {
	if ( 'preconnect' === $relation_type ) {
		$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' );
	}
	return $urls;
}
add_filter( 'wp_resource_hints', 'mliwl_resource_hints', 10, 2 );
