import sys

with open('/var/www/html/pits-new/about.html', 'r') as f:
    lines = f.readlines()

new_html = """                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 w-full mt-10">

                    <!-- Card 1 -->
                    <div class="group h-[320px] w-full [perspective:1000px]" data-aos="fade-up" data-aos-delay="0">
                        <div class="relative h-full w-full transition-transform duration-700 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
                            <!-- Front -->
                            <div class="absolute inset-0 [backface-visibility:hidden] bg-[#f8fafc] rounded-3xl p-6 flex flex-col items-center justify-center border border-slate-100 shadow-sm">
                                <div class="w-16 h-16 rounded-full bg-blue-100 flex items-center justify-center mb-6 text-blue-600 text-3xl">
                                    <i class="bi bi-shield-check"></i>
                                </div>
                                <h3 class="text-xl font-bold text-slate-800 text-center">Integrity</h3>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 [backface-visibility:hidden] [transform:rotateY(180deg)] bg-blue-600 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-lg">
                                <h3 class="text-xl font-bold text-white mb-4">Integrity</h3>
                                <p class="text-blue-50 text-sm leading-relaxed">
                                    Maintaining the highest security standards for financial data.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Card 2 -->
                    <div class="group h-[320px] w-full [perspective:1000px]" data-aos="fade-up" data-aos-delay="100">
                        <div class="relative h-full w-full transition-transform duration-700 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
                            <!-- Front -->
                            <div class="absolute inset-0 [backface-visibility:hidden] bg-[#f8fafc] rounded-3xl p-6 flex flex-col items-center justify-center border border-slate-100 shadow-sm">
                                <div class="w-16 h-16 rounded-full bg-emerald-100 flex items-center justify-center mb-6 text-emerald-600 text-3xl">
                                    <i class="bi bi-lightbulb"></i>
                                </div>
                                <h3 class="text-xl font-bold text-slate-800 text-center">Innovation</h3>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 [backface-visibility:hidden] [transform:rotateY(180deg)] bg-emerald-600 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-lg">
                                <h3 class="text-xl font-bold text-white mb-4">Innovation</h3>
                                <p class="text-emerald-50 text-sm leading-relaxed">
                                    Pioneering AI-assisted technologies for tomorrow.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Card 3 -->
                    <div class="group h-[320px] w-full [perspective:1000px]" data-aos="fade-up" data-aos-delay="200">
                        <div class="relative h-full w-full transition-transform duration-700 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
                            <!-- Front -->
                            <div class="absolute inset-0 [backface-visibility:hidden] bg-[#f8fafc] rounded-3xl p-6 flex flex-col items-center justify-center border border-slate-100 shadow-sm">
                                <div class="w-16 h-16 rounded-full bg-purple-100 flex items-center justify-center mb-6 text-purple-600 text-3xl">
                                    <i class="bi bi-cpu"></i>
                                </div>
                                <h3 class="text-xl font-bold text-slate-800 text-center">AI-Driven</h3>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 [backface-visibility:hidden] [transform:rotateY(180deg)] bg-purple-600 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-lg">
                                <h3 class="text-xl font-bold text-white mb-4">AI-Driven</h3>
                                <p class="text-purple-50 text-sm leading-relaxed">
                                    Leveraging machine learning to simplify banking processes.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Card 4 -->
                    <div class="group h-[320px] w-full [perspective:1000px]" data-aos="fade-up" data-aos-delay="300">
                        <div class="relative h-full w-full transition-transform duration-700 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
                            <!-- Front -->
                            <div class="absolute inset-0 [backface-visibility:hidden] bg-[#f8fafc] rounded-3xl p-6 flex flex-col items-center justify-center border border-slate-100 shadow-sm">
                                <div class="w-16 h-16 rounded-full bg-orange-100 flex items-center justify-center mb-6 text-orange-500 text-3xl">
                                    <i class="bi bi-headset"></i>
                                </div>
                                <h3 class="text-xl font-bold text-slate-800 text-center">Support</h3>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 [backface-visibility:hidden] [transform:rotateY(180deg)] bg-orange-500 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-lg">
                                <h3 class="text-xl font-bold text-white mb-4">Support</h3>
                                <p class="text-orange-50 text-sm leading-relaxed">
                                    Providing exceptional, 24/7 continuous assistance.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- Card 5 -->
                    <div class="group h-[320px] w-full [perspective:1000px]" data-aos="fade-up" data-aos-delay="400">
                        <div class="relative h-full w-full transition-transform duration-700 [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]">
                            <!-- Front -->
                            <div class="absolute inset-0 [backface-visibility:hidden] bg-[#f8fafc] rounded-3xl p-6 flex flex-col items-center justify-center border border-slate-100 shadow-sm">
                                <div class="w-16 h-16 rounded-full bg-red-100 flex items-center justify-center mb-6 text-red-500 text-3xl">
                                    <i class="bi bi-people"></i>
                                </div>
                                <h3 class="text-xl font-bold text-slate-800 text-center">Success Clients</h3>
                            </div>
                            <!-- Back -->
                            <div class="absolute inset-0 [backface-visibility:hidden] [transform:rotateY(180deg)] bg-red-500 rounded-3xl p-6 flex flex-col items-center justify-center text-center shadow-lg">
                                <h3 class="text-xl font-bold text-white mb-4">Success Clients</h3>
                                <p class="text-red-50 text-sm leading-relaxed">
                                    Delivering Solutions That Ensure Customer Success.
                                </p>
                            </div>
                        </div>
                    </div>

                </div>
"""

# Replace lines 108 to 262 (0-indexed 108 to 263)
new_lines = lines[:108] + [new_html] + lines[263:]

with open('/var/www/html/pits-new/about.html', 'w') as f:
    f.writelines(new_lines)

