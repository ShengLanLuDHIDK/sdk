# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

# This file contains all sources (vm and tests) for the dart virtual machine.
# Unit test files need to have a '_test' suffix appended to the name.
{
  'sources': [
    'allocation.cc',
    'allocation.h',
    'allocation_test.cc',
    'aot_optimizer.cc',
    'aot_optimizer.h',
    'assembler.cc',
    'assembler.h',
    'assembler_arm.cc',
    'assembler_arm.h',
    'assembler_arm_test.cc',
    'assembler_arm64.cc',
    'assembler_arm64.h',
    'assembler_arm64_test.cc',
    'assembler_dbc.cc',
    'assembler_dbc.h',
    'assembler_dbc_test.cc',
    'assembler_ia32.cc',
    'assembler_ia32.h',
    'assembler_ia32_test.cc',
    'assembler_test.cc',
    'assembler_x64.cc',
    'assembler_x64.h',
    'assembler_x64_test.cc',
    'assert_test.cc',
    'ast.cc',
    'ast.h',
    'ast_printer.cc',
    'ast_printer.h',
    'ast_printer_test.cc',
    'ast_test.cc',
    'ast_transformer.cc',
    'ast_transformer.h',
    'atomic.h',
    'atomic_android.h',
    'atomic_fuchsia.h',
    'atomic_linux.h',
    'atomic_macos.h',
    'atomic_simulator.h',
    'atomic_test.cc',
    'atomic_win.h',
    'base_isolate.h',
    'become.h',
    'become.cc',
    'benchmark_test.cc',
    'benchmark_test.h',
    'bigint_test.cc',
    'bit_set_test.cc',
    'bit_vector.cc',
    'bit_vector.h',
    'bit_vector_test.cc',
    'bitfield.h',
    'bitfield_test.cc',
    'bitmap.cc',
    'bitmap.h',
    'bitmap_test.cc',
    'block_scheduler.cc',
    'block_scheduler.h',
    'boolfield.h',
    'boolfield_test.cc',
    'bootstrap.h',
    'bootstrap_natives.cc',
    'bootstrap_natives.h',
    'branch_optimizer.cc',
    'branch_optimizer.h',
    'cha.cc',
    'cha.h',
    'cha_test.cc',
    'class_finalizer.cc',
    'class_finalizer.h',
    'class_finalizer_test.cc',
    'class_table.cc',
    'class_table.h',
    'clustered_snapshot.cc',
    'clustered_snapshot.h',
    'code_descriptors.cc',
    'code_descriptors.h',
    'code_descriptors_test.cc',
    'code_generator_test.cc',
    'code_observers.cc',
    'code_observers.h',
    'code_patcher.cc',
    'code_patcher.h',
    'code_patcher_arm.cc',
    'code_patcher_arm_test.cc',
    'code_patcher_arm64.cc',
    'code_patcher_arm64_test.cc',
    'code_patcher_dbc.cc',
    'code_patcher_ia32.cc',
    'code_patcher_ia32_test.cc',
    'code_patcher_x64.cc',
    'code_patcher_x64_test.cc',
    'compilation_trace.cc',
    'compilation_trace.h',
    'compiler.cc',
    'compiler.h',
    'compiler_stats.cc',
    'compiler_stats.h',
    'compiler_test.cc',
    'constant_propagator.h',
    'constant_propagator.cc',
    'constants_arm.h',
    'constants_arm64.h',
    'constants_ia32.h',
    'constants_x64.h',
    'cpu.h',
    'cpu_arm.cc',
    'cpu_arm64.cc',
    'cpu_dbc.cc',
    'cpu_ia32.cc',
    'cpu_test.cc',
    'cpu_x64.cc',
    'cpuid.h',
    'cpuid.cc',
    'cpuinfo.h',
    'cpuinfo_android.cc',
    'cpuinfo_fuchsia.cc',
    'cpuinfo_linux.cc',
    'cpuinfo_macos.cc',
    'cpuinfo_test.cc',
    'cpuinfo_win.cc',
    'custom_isolate_test.cc',
    'dart.cc',
    'dart.h',
    'dart_api_impl.h',
    'dart_api_impl_test.cc',
    'dart_api_message.cc',
    'dart_api_message.h',
    'dart_api_state.cc',
    'dart_api_state.h',
    'dart_entry.cc',
    'dart_entry.h',
    'dart_entry_test.cc',
    'datastream.h',
    'debugger.cc',
    'debugger_test.cc',
    'debugger.h',
    'debugger_api_impl_test.cc',
    'debugger_arm.cc',
    'debugger_arm64.cc',
    'debugger_dbc.cc',
    'debugger_ia32.cc',
    'debugger_x64.cc',
    'deferred_objects.cc',
    'deferred_objects.h',
    'deopt_instructions.cc',
    'deopt_instructions.h',
    'disassembler.cc',
    'disassembler.h',
    'disassembler_arm.cc',
    'disassembler_arm64.cc',
    'disassembler_dbc.cc',
    'disassembler_ia32.cc',
    'disassembler_test.cc',
    'disassembler_x64.cc',
    'double_conversion.cc',
    'double_conversion.h',
    'double_internals.h',
    'dwarf.cc',
    'dwarf.h',
    'exceptions.cc',
    'exceptions.h',
    'exceptions_test.cc',
    'find_code_object_test.cc',
    'fixed_cache.h',
    'fixed_cache_test.cc',
    'flag_list.h',
    'flags.cc',
    'flags.h',
    'flags_test.cc',
    'flow_graph.cc',
    'flow_graph.h',
    'flow_graph_allocator.cc',
    'flow_graph_allocator.h',
    'flow_graph_builder.cc',
    'flow_graph_builder.h',
    'flow_graph_builder_test.cc',
    'flow_graph_compiler.cc',
    'flow_graph_compiler.h',
    'flow_graph_compiler_arm.cc',
    'flow_graph_compiler_arm64.cc',
    'flow_graph_compiler_dbc.cc',
    'flow_graph_compiler_ia32.cc',
    'flow_graph_compiler_x64.cc',
    'flow_graph_inliner.cc',
    'flow_graph_inliner.h',
    'flow_graph_range_analysis.cc',
    'flow_graph_range_analysis.h',
    'flow_graph_range_analysis_test.cc',
    'flow_graph_type_propagator.cc',
    'flow_graph_type_propagator.h',
    'freelist.cc',
    'freelist.h',
    'freelist_test.cc',
    'gc_marker.cc',
    'gc_marker.h',
    'gc_sweeper.cc',
    'gc_sweeper.h',
    'gdb_helpers.cc',
    'globals.h',
    'growable_array.h',
    'growable_array_test.cc',
    'guard_field_test.cc',
    'handles.cc',
    'handles.h',
    'handles_impl.h',
    'handles_test.cc',
    'hash_map.h',
    'hash_map_test.cc',
    'hash_table.h',
    'hash_table_test.cc',
    'heap.cc',
    'heap.h',
    'heap_test.cc',
    'il_printer.cc',
    'il_printer.h',
    'instructions.h',
    'instructions_arm.cc',
    'instructions_arm.h',
    'instructions_arm_test.cc',
    'instructions_arm64.cc',
    'instructions_arm64.h',
    'instructions_arm64_test.cc',
    'instructions_dbc.cc',
    'instructions_dbc.h',
    'instructions_ia32.cc',
    'instructions_ia32.h',
    'instructions_ia32_test.cc',
    'instructions_x64.cc',
    'instructions_x64.h',
    'instructions_x64_test.cc',
    'intermediate_language.cc',
    'intermediate_language.h',
    'intermediate_language_arm.cc',
    'intermediate_language_arm64.cc',
    'intermediate_language_dbc.cc',
    'intermediate_language_ia32.cc',
    'intermediate_language_test.cc',
    'intermediate_language_x64.cc',
    'intrinsifier.cc',
    'intrinsifier.h',
    'intrinsifier_arm.cc',
    'intrinsifier_arm64.cc',
    'intrinsifier_dbc.cc',
    'intrinsifier_ia32.cc',
    'intrinsifier_x64.cc',
    'isolate.cc',
    'isolate.h',
    'isolate_reload.cc',
    'isolate_reload.h',
    'isolate_reload_test.cc',
    'isolate_test.cc',
    'jit_optimizer.cc',
    'jit_optimizer.h',
    'json_parser.h',
    'json_stream.h',
    'json_stream.cc',
    'json_test.cc',
    'kernel_isolate.cc',
    'kernel_isolate.h',
    'locations.cc',
    'locations.h',
    'lockers.cc',
    'lockers.h',
    'log_test.cc',
    'log.cc',
    'log.h',
    'longjump.cc',
    'longjump.h',
    'longjump_test.cc',
    'malloc_hooks_jemalloc.cc',
    'malloc_hooks_tcmalloc.cc',
    'malloc_hooks_arm.cc',
    'malloc_hooks_arm64.cc',
    'malloc_hooks_ia32.cc',
    'malloc_hooks_x64.cc',
    'malloc_hooks.h',
    'malloc_hooks_test.cc',
    'malloc_hooks_unsupported.cc',
    'megamorphic_cache_table.cc',
    'megamorphic_cache_table.h',
    'memory_region.cc',
    'memory_region.h',
    'memory_region_test.cc',
    'message.cc',
    'message.h',
    'message_handler.cc',
    'message_handler.h',
    'message_handler_test.cc',
    'message_test.cc',
    'method_recognizer.cc',
    'method_recognizer.h',
    'metrics.cc',
    'metrics.h',
    'metrics_test.cc',
    'native_arguments.h',
    'native_entry.cc',
    'native_entry.h',
    'native_entry_test.cc',
    'native_entry_test.h',
    'native_message_handler.cc',
    'native_message_handler.h',
    'native_symbol.h',
    'native_symbol_android.cc',
    'native_symbol_fuchsia.cc',
    'native_symbol_linux.cc',
    'native_symbol_macos.cc',
    'native_symbol_win.cc',
    'object.cc',
    'object.h',
    'object_arm_test.cc',
    'object_arm64_test.cc',
    'object_dbc_test.cc',
    'object_graph.cc',
    'object_graph.h',
    'object_graph_test.cc',
    'object_ia32_test.cc',
    'object_id_ring.cc',
    'object_id_ring.h',
    'object_id_ring_test.cc',
    'object_reload.cc',
    'object_service.cc',
    'object_set.h',
    'object_store.cc',
    'object_store.h',
    'object_store_test.cc',
    'object_test.cc',
    'object_x64_test.cc',
    'optimizer.cc',
    'optimizer.h',
    'os.h',
    'os_android.cc',
    'os_fuchsia.cc',
    'os_linux.cc',
    'os_macos.cc',
    'os_test.cc',
    'os_thread.cc',
    'os_thread.h',
    'os_thread_android.cc',
    'os_thread_android.h',
    'os_thread_fuchsia.cc',
    'os_thread_fuchsia.h',
    'os_thread_linux.cc',
    'os_thread_linux.h',
    'os_thread_macos.cc',
    'os_thread_macos.h',
    'os_thread_win.cc',
    'os_thread_win.h',
    'os_win.cc',
    'pages.cc',
    'pages.h',
    'pages_test.cc',
    'parser.cc',
    'parser.h',
    'parser_test.cc',
    'port.cc',
    'port.h',
    'port_test.cc',
    'precompiler.cc',
    'precompiler.h',
    'program_visitor.cc',
    'program_visitor.h',
    'kernel.h',
    'kernel.cc',
    'kernel_binary.cc',
    'kernel_binary.h',
    'kernel_binary_flowgraph.cc',
    'kernel_binary_flowgraph.h',
    'kernel_to_il.cc',
    'kernel_to_il.h',
    'kernel_reader.h',
    'kernel_reader.cc',
    'proccpuinfo.cc',
    'proccpuinfo.h',
    'profiler_service.cc',
    'profiler_service.h',
    'profiler_test.cc',
    'profiler.cc',
    'profiler.h',
    'random.cc',
    'random.h',
    'raw_object.cc',
    'raw_object.h',
    'raw_object_snapshot.cc',
    'redundancy_elimination.cc',
    'redundancy_elimination.h',
    'regexp.cc',
    'regexp.h',
    'regexp_assembler.cc',
    'regexp_assembler.h',
    'regexp_assembler_bytecode.cc',
    'regexp_assembler_bytecode.h',
    'regexp_assembler_bytecode_inl.h',
    'regexp_assembler_ir.cc',
    'regexp_assembler_ir.h',
    'regexp_ast.cc',
    'regexp_ast.h',
    'regexp_bytecodes.h',
    'regexp_interpreter.cc',
    'regexp_interpreter.h',
    'regexp_parser.cc',
    'regexp_parser.h',
    'regexp_test.cc',
    'report.cc',
    'report.h',
    'resolver.cc',
    'resolver.h',
    'resolver_test.cc',
    'reusable_handles.h',
    'ring_buffer.h',
    'ring_buffer_test.cc',
    'runtime_entry.h',
    'runtime_entry_list.h',
    'runtime_entry_arm.cc',
    'runtime_entry_arm64.cc',
    'runtime_entry_dbc.cc',
    'runtime_entry_ia32.cc',
    'runtime_entry.cc',
    'runtime_entry_x64.cc',
    'safepoint.cc',
    'safepoint.h',
    'scanner.cc',
    'scanner.h',
    'scanner_test.cc',
    'scavenger.cc',
    'scavenger.h',
    'scavenger_test.cc',
    'scope_timer.h',
    'scopes.cc',
    'scopes.h',
    'scopes_test.cc',
    'service.cc',
    'service.h',
    'service_event.cc',
    'service_event.h',
    'service_isolate.cc',
    'service_isolate.h',
    'service_test.cc',
    'signal_handler_android.cc',
    'signal_handler_fuchsia.cc',
    'signal_handler_linux.cc',
    'signal_handler_macos.cc',
    'signal_handler_win.cc',
    'signal_handler.h',
    'simulator.h',
    'simulator_arm.cc',
    'simulator_arm.h',
    'simulator_arm64.cc',
    'simulator_arm64.h',
    'simulator_dbc.cc',
    'simulator_dbc.h',
    'snapshot.cc',
    'snapshot.h',
    'snapshot_ids.h',
    'snapshot_test.cc',
    'source_report.cc',
    'source_report.h',
    'source_report_test.cc',
    'spaces.h',
    'stack_frame.cc',
    'stack_frame.h',
    'stack_frame_arm.h',
    'stack_frame_arm64.h',
    'stack_frame_ia32.h',
    'stack_frame_test.cc',
    'stack_frame_x64.h',
    'stack_trace.cc',
    'stack_trace.h',
    'store_buffer.cc',
    'store_buffer.h',
    'stub_code.cc',
    'stub_code.h',
    'stub_code_arm.cc',
    'stub_code_arm_test.cc',
    'stub_code_arm64.cc',
    'stub_code_arm64_test.cc',
    'stub_code_dbc.cc',
    'stub_code_ia32.cc',
    'stub_code_ia32_test.cc',
    'stub_code_x64.cc',
    'stub_code_x64_test.cc',
    'symbols.cc',
    'symbols.h',
    'tags.cc',
    'tags.h',
    'thread.cc',
    'thread.h',
    'thread_barrier.h',
    'thread_barrier_test.cc',
    'thread_interrupter.cc',
    'thread_interrupter.h',
    'thread_interrupter_android.cc',
    'thread_interrupter_fuchsia.cc',
    'thread_interrupter_linux.cc',
    'thread_interrupter_macos.cc',
    'thread_interrupter_win.cc',
    'thread_pool.cc',
    'thread_pool.h',
    'thread_pool_test.cc',
    'thread_registry.cc',
    'thread_registry.h',
    'thread_test.cc',
    'timeline.cc',
    'timeline.h',
    'timeline_analysis.cc',
    'timeline_analysis.h',
    'timeline_android.cc',
    'timeline_fuchsia.cc',
    'timeline_linux.cc',
    'timeline_macos.cc',
    'timeline_test.cc',
    'timeline_win.cc',
    'timer.cc',
    'timer.h',
    'token.cc',
    'token.h',
    'token_position.cc',
    'token_position.h',
    'type_table.h',
    'unibrow.cc',
    'unibrow.h',
    'unibrow-inl.h',
    'unicode.cc',
    'unicode.h',
    'unicode_data.cc',
    'unicode_test.cc',
    'unit_test.cc',
    'unit_test.h',
    'uri.cc',
    'uri.h',
    'uri_test.cc',
    'utils_test.cc',
    'verifier.cc',
    'verifier.h',
    'virtual_memory.cc',
    'virtual_memory.h',
    'virtual_memory_android.cc',
    'virtual_memory_fuchsia.cc',
    'virtual_memory_linux.cc',
    'virtual_memory_macos.cc',
    'virtual_memory_test.cc',
    'virtual_memory_win.cc',
    'visitor.h',
    'weak_code.cc',
    'weak_code.h',
    'weak_table.cc',
    'weak_table.h',
    'zone.cc',
    'zone.h',
    'zone_test.cc',
    'zone_text_buffer.cc',
    'zone_text_buffer.h',
  ],
}
