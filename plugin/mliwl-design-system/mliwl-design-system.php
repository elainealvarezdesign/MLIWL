<?php
/**
 * Plugin Name:       MLIWL Design System
 * Plugin URI:        https://mylifeisworthliving.org
 * Description:       Design tokens, component classes and the mobile-menu script for My Life Is Worth Living. Works with any theme (Astra, Hello Elementor…) and Elementor Pro.
 * Version:           0.3.0
 * Requires at least: 6.0
 * Requires PHP:      7.4
 * Author:            MLIWL design team
 * License:           GPL-2.0-or-later
 * Text Domain:       mliwl
 *
 * @package mliwl
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'MLIWL_DS_VERSION', '0.3.0' );
define( 'MLIWL_DS_URL', plugin_dir_url( __FILE__ ) );

/**
 * Brand font, tokens and components.
 *
 * Loaded late (priority 999) and after the theme and Elementor stylesheets, so the
 * MLIWL classes win over Astra's and Elementor's defaults without !important.
 */
function mliwl_ds_enqueue_styles() {
	$after = array();
	foreach ( array( 'astra-theme-css', 'hello-elementor', 'elementor-frontend', 'elementor-pro' ) as $handle ) {
		if ( wp_style_is( $handle, 'registered' ) ) {
			$after[] = $handle;
		}
	}

	wp_enqueue_style(
		'mliwl-font',
		'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;800;900&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'mliwl-tokens', MLIWL_DS_URL . 'assets/css/tokens.css', $after, MLIWL_DS_VERSION );
	wp_enqueue_style( 'mliwl-components', MLIWL_DS_URL . 'assets/css/components.css', array( 'mliwl-tokens', 'mliwl-font' ), MLIWL_DS_VERSION );
	wp_enqueue_style( 'mliwl-sections', MLIWL_DS_URL . 'assets/css/sections.css', array( 'mliwl-components' ), MLIWL_DS_VERSION );
}
add_action( 'wp_enqueue_scripts', 'mliwl_ds_enqueue_styles', 999 );

/**
 * Same styles inside the Elementor editor preview, so editors see the real result.
 */
add_action( 'elementor/preview/enqueue_styles', 'mliwl_ds_enqueue_styles' );

/**
 * Mobile menu: the header's Menu button opens the "MLIWL Mobile Menu" popup.
 * Finds the popup by its title so no ID has to be typed in after importing.
 */
function mliwl_ds_enqueue_mobile_menu() {
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
	wp_enqueue_script( 'mliwl-mobile-menu', MLIWL_DS_URL . 'assets/js/mobile-menu.js', array( 'jquery' ), MLIWL_DS_VERSION, true );
	wp_localize_script( 'mliwl-mobile-menu', 'mliwlMenu', array( 'popupId' => (int) $popups[0] ) );
}
add_action( 'wp_enqueue_scripts', 'mliwl_ds_enqueue_mobile_menu', 999 );

/**
 * Preconnect to Google Fonts for a faster first paint.
 *
 * @param array  $urls          URLs to print for resource hints.
 * @param string $relation_type The relation type the URLs are printed for.
 * @return array
 */
function mliwl_ds_resource_hints( $urls, $relation_type ) {
	if ( 'preconnect' === $relation_type ) {
		$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' );
	}
	return $urls;
}
add_filter( 'wp_resource_hints', 'mliwl_ds_resource_hints', 10, 2 );

/**
 * Admin notice when Elementor Pro is missing: the header, footer and menu templates need it.
 */
function mliwl_ds_requirements_notice() {
	if ( defined( 'ELEMENTOR_PRO_VERSION' ) || ! current_user_can( 'activate_plugins' ) ) {
		return;
	}
	echo '<div class="notice notice-warning"><p>' . esc_html__( 'MLIWL Design System: the header, footer and mobile menu templates need Elementor Pro. The styles still load without it.', 'mliwl' ) . '</p></div>';
}
add_action( 'admin_notices', 'mliwl_ds_requirements_notice' );
